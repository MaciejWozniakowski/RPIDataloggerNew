import 'package:flutter/material.dart';

void main() {
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

  Future<void> _pickDateTime(BuildContext context, bool isFirstButton) async {
    // Step 1: Select Date
    final DateTime? pickedDate = await showDatePicker(
      context: context,
      initialDate: DateTime.now(),
      firstDate: DateTime(2000),
      lastDate: DateTime(2100),
    );

    if (pickedDate != null) {
      // Step 2: Select Time
      final TimeOfDay? pickedTime = await showTimePicker(
        context: context,
        initialTime: TimeOfDay.now(),
      );

      if (pickedTime != null) {
        // Combine date and time
        final DateTime combinedDateTime = DateTime(
          pickedDate.year,
          pickedDate.month,
          pickedDate.day,
          pickedTime.hour,
          pickedTime.minute,
        );

        // Format date and time as string
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
                // Dropdown Elevated Button
                Builder(
                  builder: (context) => ElevatedButton(
                    onPressed: () => _showDropdown(context),
                    child: Text(_dropdownValue),
                  ),
                ),
                // Date-Time Picker Buttons
                ElevatedButton(
                  onPressed: () => _pickDateTime(context, true),
                  child: Text(_selectedDateTime1),
                ),
                ElevatedButton(
                  onPressed: () => _pickDateTime(context, false),
                  child: Text(_selectedDateTime2),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

