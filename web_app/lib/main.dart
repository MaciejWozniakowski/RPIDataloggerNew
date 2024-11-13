import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Datalogger Query Web App'),
        ),
        body: DateDropdowns(),
      ),
    );
  }
}

class DateDropdowns extends StatefulWidget {
  @override
  _DateDropdownsState createState() => _DateDropdownsState();
}

class _DateDropdownsState extends State<DateDropdowns> {
  List<DateTime> dateList = [];
  DateTime? selectedDate1;
  DateTime? selectedDate2;
  String? selectedMeter;

  final List<String> meters = ["Meter 1", "Meter 2", "Meter 3"];

  @override
  void initState() {
    super.initState();
    _generateDateList();
  }

  void _generateDateList() {
    DateTime today = DateTime.now();
    for (int i = 0; i < 30; i++) {
      dateList.add(today.add(Duration(days: i)));
    }
  }

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(16.0),
      child: Column(
        children: [
          Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text("Meter Select"),
              DropdownButton<String>(
                value: selectedMeter,
                items: meters.map((String meter) {
                  return DropdownMenuItem<String>(
                    value: meter,
                    child: Text(meter, style: TextStyle(fontSize: 16)),
                  );
                }).toList(),
                onChanged: (String? newMeter) {
                  setState(() {
                    selectedMeter = newMeter;
                  });
                },
              ),
            ],
          ),
          SizedBox(height: 20),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text("Select Start Date"),
                  DropdownButton<DateTime>(
                    value: selectedDate1,
                    items: dateList.map((DateTime date) {
                      return DropdownMenuItem<DateTime>(
                        value: date,
                        child: Text(
                          "${date.day}/${date.month}/${date.year}",
                          style: TextStyle(fontSize: 16),
                        ),
                      );
                    }).toList(),
                    onChanged: (DateTime? newDate) {
                      setState(() {
                        selectedDate1 = newDate;
                      });
                    },
                  ),
                ],
              ),
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text("Select End Date"),
                  DropdownButton<DateTime>(
                    value: selectedDate2,
                    items: dateList.map((DateTime date) {
                      return DropdownMenuItem<DateTime>(
                        value: date,
                        child: Text(
                          "${date.day}/${date.month}/${date.year}",
                          style: TextStyle(fontSize: 16),
                        ),
                      );
                    }).toList(),
                    onChanged: (DateTime? newDate) {
                      setState(() {
                        selectedDate2 = newDate;
                      });
                    },
                  ),
                ],
              ),
            ],
          ),
          SizedBox(height: 20),
          if (selectedDate1 != null && selectedDate2 != null)
            Text(
              "Selected Start Date: ${selectedDate1!.day}/${selectedDate1!.month}/${selectedDate1!.year}\n"
              "Selected End Date: ${selectedDate2!.day}/${selectedDate2!.month}/${selectedDate2!.year}",
              style: TextStyle(fontSize: 16),
              textAlign: TextAlign.center,
            ),
          SizedBox(height: 20),
          Expanded(
            child: Container(
              color: Colors.grey[200],
              child: Center(
                child: Text(
                  "Table Placeholder",
                  style: TextStyle(fontSize: 20, color: Colors.black54),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
