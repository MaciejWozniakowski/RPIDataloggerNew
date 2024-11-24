import 'package:flutter/material.dart';
import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';

void main() {
  runApp(MyApp());
}


/*
Future<List<Map<String, dynamic>>> fetchData() async {
  // Open database connection
  final database = openDatabase(
    join(await getDatabasesPath(), 'example.db'),
  );

  // Execute query
  final db = await database;
  return await db.query('your_table_name');
}


Future<DataTable> buildTable() async {
  List<Map<String, dynamic>> queryResult = await fetchData();
  List<DataRow> rows = queryResult.map((data) {
    return DataRow(
      cells: data.values.map((value) => DataCell(Text(value.toString()))).toList(),
    );
  }).toList();

  return DataTable(
    columns: queryResult.isEmpty
        ? []
        : queryResult.first.keys.map((key) => DataColumn(label: Text(key))).toList(),
    rows: rows,
  );
}

class SQLTableScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('SQL Data Table'),
      ),
      body: FutureBuilder<DataTable>(
        future: buildTable(),
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          } else if (snapshot.hasData) {
            return SingleChildScrollView(
              scrollDirection: Axis.horizontal, // For horizontal scrolling
              child: SingleChildScrollView(
                scrollDirection: Axis.vertical, // For vertical scrolling
                child: snapshot.data,
              ),
            );
          } else {
            return Center(child: Text('No data available'));
          }
        },
      ),
    );
  }
}
*/
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Datalogger Query Web App'),
        ),
        body: DateDropdowns(),
      )
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
                  "Tutaj będzie tabela z pomiarami ",
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
