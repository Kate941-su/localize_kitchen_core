// Flutter Usage Example for Parameterized Strings
// This file demonstrates how to use the generated ARB files with parameters

import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Localization Demo',
      localizationsDelegates: [
        AppLocalizations.delegate,
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
        GlobalCupertinoLocalizations.delegate,
      ],
      supportedLocales: [
        Locale('en', ''), // English
        Locale('ja', ''), // Japanese
      ],
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context)!;
    
    return Scaffold(
      appBar: AppBar(
        title: Text('Parameterized Strings Demo'),
      ),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Simple greeting
            Text(
              l10n.greeting,
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 20),
            
            // Parameterized strings examples
            _buildParameterizedExample(
              'Welcome Message:',
              l10n.welcome_message('John'),
            ),
            
            _buildParameterizedExample(
              'Item Count:',
              l10n.item_count(5),
            ),
            
            _buildParameterizedExample(
              'Price Format:',
              l10n.price_format(99.99),
            ),
            
            _buildParameterizedExample(
              'Date Format:',
              l10n.date_format('Monday', 'January', '15'),
            ),
            
            _buildParameterizedExample(
              'Complex Message:',
              l10n.complex_message('Alice', 3, 'Bob'),
            ),
          ],
        ),
      ),
    );
  }
  
  Widget _buildParameterizedExample(String label, String value) {
    return Padding(
      padding: EdgeInsets.symmetric(vertical: 8.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            label,
            style: TextStyle(fontWeight: FontWeight.bold, color: Colors.grey[600]),
          ),
          Text(
            value,
            style: TextStyle(fontSize: 16),
          ),
        ],
      ),
    );
  }
}

// pubspec.yaml dependencies needed:
/*
dependencies:
  flutter:
    sdk: flutter
  flutter_localizations:
    sdk: flutter

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_gen_runner:
*/

// l10n.yaml configuration:
/*
arb-dir: sample_output/dart
template-arb-file: app_en.arb
output-localization-file: app_localizations.dart
output-class: AppLocalizations
*/

// Generated Dart code usage:
/*
// After running flutter gen-l10n, you can use:

// Simple string
String greeting = AppLocalizations.of(context)!.greeting;

// Parameterized strings
String welcome = AppLocalizations.of(context)!.welcome_message('John');
String itemCount = AppLocalizations.of(context)!.item_count(5);
String price = AppLocalizations.of(context)!.price_format(99.99);
String date = AppLocalizations.of(context)!.date_format('Monday', 'January', '15');
String complex = AppLocalizations.of(context)!.complex_message('Alice', 3, 'Bob');
*/
