import 'package:flutter/material.dart';
import 'package:flutter_py/flutter_py.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: Text('ChowBot AI Food Analyzer')),
        body: FoodAnalyzer(),
      ),
    );
  }
}

class FoodAnalyzer extends StatefulWidget {
  @override
  _FoodAnalyzerState createState() => _FoodAnalyzerState();
}

class _FoodAnalyzerState extends State<FoodAnalyzer> {
  String _result = "Upload an image to start analysis.";

  Future<void> _analyzeFood() async {
    final foodItem = await FlutterPy().runPythonFunction(
      scriptPath: 'chowbot.py',
      functionName: 'predict_from_image',
      args: ['path_to_image'],
    );
    final analysis = await FlutterPy().runPythonFunction(
      scriptPath: 'chowbot.py',
      functionName: 'analyze_with_gemini',
      args: ['your_gemini_api_key', foodItem],
    );
    setState(() {
      _result = analysis;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        ElevatedButton(
          onPressed: _analyzeFood,
          child: Text('Analyze Food'),
        ),
        SizedBox(height: 20),
        Text(_result),
      ],
    );
  }
}
