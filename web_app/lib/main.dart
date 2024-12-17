import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:csv/csv.dart';


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

class DateTimePickerButtons extends StatefulWidget {
  const DateTimePickerButtons({Key? key}) : super(key: key);

  @override
  _DateTimePickerButtonsState createState() => _DateTimePickerButtonsState();
}

class _DateTimePickerButtonsState extends State<DateTimePickerButtons> {
  String _selectedDateTime1 = "Select start date";
  String _selectedDateTime2 = "Select end date";
  String _dropdownValue = "Meter select";

  // State variable for holding query results
  List<dynamic> _queryResults = [];

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
                "${combinedDateTime.hour.toString().padLeft(2, '0')}:${combinedDateTime.minute.toString().padLeft(2, '0')}";
          } else {
            _selectedDateTime2 =
                "${combinedDateTime.year}-${combinedDateTime.month.toString().padLeft(2, '0')}-${combinedDateTime.day.toString().padLeft(2, '0')} "
                "${combinedDateTime.hour.toString().padLeft(2, '0')}:${combinedDateTime.minute.toString().padLeft(2, '0')}";
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

  Future<void> _fetchAndDisplayData() async {
    try {
      final url = Uri.parse(
          'http://127.0.0.1:5000/api/query?meter=$_dropdownValue&start_date=$_selectedDateTime1&end_date=$_selectedDateTime2');

      final response = await http.get(url);
      print(response);

      if (response.statusCode == 200) {
        List<dynamic> responseData = json.decode(response.body);

        setState(() {
          _queryResults = responseData; // Update state with query results
        });
      } else {
        _showErrorDialog("Failed to load data. Status code: ${response.statusCode}");
      }
    } catch (e) {
      _showErrorDialog("Error: $e");
    }
  }

  void _showErrorDialog(String message) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text("Error"),
        content: Text(message),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text("OK"),
          ),
        ],
      ),
    );
  }

  Future<void> _downloadCSV() async {
    if (_queryResults.isEmpty) {
      _showErrorDialog("No data to download");
      return;
    }
    String csv = '';
    for(var row in _queryResults){
      List<String> rowData = row.values.map((value) => value.toString()).toList();
    csv += rowData.join(',') + '\n';
  }
    

    final url = Uri.dataFromString(csv, mimeType: 'text/csv');

    http.get(url).then((response) {
      if (response.statusCode == 200) {
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(
            content: Text('CSV file downloaded successfully!'),
            backgroundColor: Colors.green,
          ),
        );
      } else {
        _showErrorDialog('Failed to download CSV file.');
      }
    });
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
                      _fetchAndDisplayData();
                    } else {
                      _showErrorDialog("Please select all required values.");
                    }
                  },
                  child: const Text("Display data"),
                ),
                ElevatedButton(
                  onPressed: () => _downloadCSV(),

                  child: const Text("Download as CSV")
                )
              ],
            ),
          ),
          Expanded(
            child: _queryResults.isNotEmpty
                ? SingleChildScrollView(
                    scrollDirection: Axis.horizontal,
                    child: DataTable(
                      columns: _queryResults.first.keys.map<DataColumn>((key) => DataColumn(label: Text(key))).toList(),
                      rows: _queryResults.map<DataRow>((item) {
                        return DataRow(
                          cells: item.values.map<DataCell>((value) => DataCell(Text(value.toString()))).toList(),
                        );
                      }).toList(),
                    ),
                  )
                : const Center(
                    child: Text("No data to display"),
                  ),
          ),
        ],
      ),
    );
  }
}


