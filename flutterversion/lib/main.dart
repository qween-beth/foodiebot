import 'dart:convert';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:image_picker/image_picker.dart';  // Import for image picking
import 'package:serious_python/serious_python.dart';

void main() {
  startPython();  // Initialize the Python environment
  runApp(const MyApp());
}

void startPython() async {
  // Start the Python environment from the specified zip file
  SeriousPython.run("app/app.zip", environmentVariables: {"a": "1", "b": "2"});
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  String _result = "Upload an image to start analysis.";
  bool _isLoading = false;
  File? _image;  // To store the selected image

  Future<void> _pickImage() async {
    final picker = ImagePicker();
    final pickedFile = await picker.pickImage(source: ImageSource.gallery);

    if (pickedFile != null) {
      setState(() {
        _image = File(pickedFile.path);
      });
    }
  }

  Future<void> _analyzeFood() async {
    if (_image == null) {
      setState(() {
        _result = "Please upload an image first.";
      });
      return;
    }

    setState(() {
      _isLoading = true;  // Show loading indicator
    });

    try {
      // Call the Python function to analyze the image and get the food item
      final foodItemResponse = await http.post(
        Uri.parse("http://127.0.0.1:55818"),
        body: jsonEncode({
          "scriptPath": "chowbot.py",
          "functionName": "predict_from_image",
          "args": [_image!.path]  // Pass the image path here
        }),
        headers: {"Content-Type": "application/json"},
      );

      String foodItem = foodItemResponse.body;

      // Call another Python function to analyze the food item with Gemini AI
      final analysisResponse = await http.post(
        Uri.parse("http://127.0.0.1:55818"),
        body: jsonEncode({
          "scriptPath": "chowbot.py",
          "functionName": "analyze_with_gemini",
          "args": ["your_gemini_api_key", foodItem]
        }),
        headers: {"Content-Type": "application/json"},
      );

      setState(() {
        _result = analysisResponse.body;
      });
    } catch (e) {
      setState(() {
        _result = "An error occurred: $e";
      });
    } finally {
      setState(() {
        _isLoading = false;  // Hide loading indicator
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('ChowBot AI Food Analyzer')),
        body: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            children: [
              _image == null
                  ? const Text('No image selected.')
                  : Image.file(_image!, height: 200),
              const SizedBox(height: 20),
              ElevatedButton(
                onPressed: _pickImage,  // Button to upload image
                child: const Text('Upload Image'),
              ),
              const SizedBox(height: 20),
              ElevatedButton(
                onPressed: _analyzeFood,  // Button to analyze food
                child: const Text('Analyze Food'),
              ),
              const SizedBox(height: 20),
              _isLoading
                  ? const CircularProgressIndicator()
                  : Text(_result, style: const TextStyle(fontSize: 16)),
            ],
          ),
        ),
      ),
    );
  }
}
