import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

Future<void> main() async {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Datalogger Query App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const DateTimePickerButtons(),
    );
  }
}

Future<void> openAndQueryDatabase(
    String meter, String startDate, String endDate) async {
  try {
    // Construct the API URL with parameters, including the meter name
    final url = Uri.parse(
        'http://127.0.0.1:5000/api/query?meter=$meter&start_date=$startDate&end_date=$endDate');

    // Send a GET request to the API
    final response = await http.get(url);

    if (response.statusCode == 200) {
      // Parse the response if status code is OK
      List<dynamic> responseData = json.decode(response.body);

      if (responseData.isNotEmpty) {
        // If data is returned, print the results
        print('Query Results:');
        for (var item in responseData) {
          print(item);
        }
      } else {
        // No data found
        print('No data found for the given meter and date range');
      }
    } else {
      // Handle non-200 status codes
      print('Failed to load data. Status code: ${response.statusCode}');
    }
  } catch (e) {
    // Handle any errors
    print('Error: $e');
  }
}

class DateTimePickerButtons extends StatefulWidget {
  const DateTimePickerButtons({Key? key}) : super(key: key);

  @override
  _DateTimePickerButtonsState createState() => _DateTimePickerButtonsState();
}

class _DateTimePickerButtonsState extends State<DateTimePickerButtons> {
  String _selectedDateTime1 = "Select start date";
  String _selectedDateTime2 = "Select end date";
  String _dropdownValue = "Meter select";

  Future<void> _pickDateTime(BuildContext context, bool isFirstButton) async {
    final DateTime? pickedDate = await showDatePicker(
      context: context,
      initialDate: DateTime.now(),
      firstDate: DateTime(2000),
      lastDate: DateTime(2100),
    );

    if (pickedDate != null) {
      final TimeOfDay? pickedTime = await showTimePicker(
        context: context,
        initialTime: TimeOfDay.now(),
      );

      if (pickedTime != null) {
        final DateTime combinedDateTime = DateTime(
          pickedDate.year,
          pickedDate.month,
          pickedDate.day,
          pickedTime.hour,
          pickedTime.minute,
        );

        setState(() {
          if (isFirstButton) {
            _selectedDateTime1 =
                "${combinedDateTime.year}-${combinedDateTime.month.toString().padLeft(2, '0')}-${combinedDateTime.day.toString().padLeft(2, '0')} "
                "${combinedDateTime.hour.toString().padLeft(2, '0')}:${combinedDateTime.minute.toString().padLeft(2, '0')}:${combinedDateTime.second.toString().padLeft(2, '0')}";
          } else {
            _selectedDateTime2 =
                "${combinedDateTime.year}-${combinedDateTime.month.toString().padLeft(2, '0')}-${combinedDateTime.day.toString().padLeft(2, '0')} "
                "${combinedDateTime.hour.toString().padLeft(2, '0')}:${combinedDateTime.minute.toString().padLeft(2, '0')}:${combinedDateTime.second.toString().padLeft(2, '0')}";
          }
        });
      }
    }
  }

  Future<void> _showDropdown(BuildContext context) async {
    final RenderBox button = context.findRenderObject() as RenderBox;
    final Offset buttonPosition = button.localToGlobal(Offset.zero);
    final String? selectedValue = await showMenu<String>(
      context: context,
      position: RelativeRect.fromLTRB(
        buttonPosition.dx,
        buttonPosition.dy + button.size.height,
        buttonPosition.dx + button.size.width,
        buttonPosition.dy,
      ),
      items: <PopupMenuEntry<String>>[
        const PopupMenuItem<String>(value: "DCmeter_89", child: Text("DCmeter_89")),
        const PopupMenuItem<String>(value: "DCmeter_21", child: Text("DCmeter_21")),
        const PopupMenuItem<String>(value: "DCmeter_83", child: Text("DCmeter_83")),
        const PopupMenuItem<String>(value: "DCmeter_57", child: Text("DCmeter_57")),
        const PopupMenuItem<String>(value: "DCmeter_3_1", child: Text("DCmeter_3_1")),
        const PopupMenuItem<String>(value: "DCmeter_3_2", child: Text("DCmeter_3_2")),
        const PopupMenuItem<String>(value: "ACmeter", child: Text("ACmeter")),
      ],
    );

    if (selectedValue != null) {
      setState(() {
        _dropdownValue = selectedValue;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Datalogger Query App'),
      ),
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Padding(
            padding: const EdgeInsets.all(16.0),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                Builder(
                  builder: (context) => ElevatedButton(
                    onPressed: () => _showDropdown(context),
                    child: Text(_dropdownValue),
                  ),
                ),
                ElevatedButton(
                  onPressed: () => _pickDateTime(context, true),
                  child: Text(_selectedDateTime1),
                ),
                ElevatedButton(
                  onPressed: () => _pickDateTime(context, false),
                  child: Text(_selectedDateTime2),
                ),
                ElevatedButton(
                  onPressed: () {
                    if (_dropdownValue != "Meter select" &&
                        _selectedDateTime1 != "Select start date" &&
                        _selectedDateTime2 != "Select end date") {
                      openAndQueryDatabase(
                          _dropdownValue, _selectedDateTime1, _selectedDateTime2);
                    } else {
                      showDialog(
                        context: context,
                        builder: (context){
                          return AlertDialog(
                            title: TextField(
                              decoration:  const InputDecoration(hintText: "Please select all required values"),
                            ),);
                        },
                      );
                    }
                  },
                  child: const Text("Display data"),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
