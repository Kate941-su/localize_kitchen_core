// Xcode Usage Example for .xcstrings Localization
// This file demonstrates how to use the generated .xcstrings file in iOS/macOS apps

import Foundation

class LocalizationExample {
    
    // MARK: - Basic String Usage
    
    func basicStringExamples() {
        // Simple strings
        let greeting = NSLocalizedString("greeting", comment: "Greeting message")
        print(greeting) // Output: "Hello" (or localized version)
        
        let frog = NSLocalizedString("frog", comment: "Animal name")
        print(frog) // Output: "frog" (or localized version)
    }
    
    // MARK: - Parameterized String Usage
    
    func parameterizedStringExamples() {
        // For strings with parameters, you need to use String.localizedStringWithFormat
        // Note: The .xcstrings file contains the parameterized strings, but you need to
        // convert them to use %@ format for String.localizedStringWithFormat
        
        // Example with one parameter
        let welcomeFormat = NSLocalizedString("welcome_message", comment: "Welcome message with name")
        let welcomeMessage = String.localizedStringWithFormat(welcomeFormat, "John")
        print(welcomeMessage) // Output: "Welcome, John!" (or localized version)
        
        // Example with multiple parameters
        let itemCountFormat = NSLocalizedString("item_count", comment: "Item count message")
        let itemCountMessage = String.localizedStringWithFormat(itemCountFormat, 5)
        print(itemCountMessage) // Output: "You have 5 items" (or localized version)
        
        // Example with price formatting
        let priceFormat = NSLocalizedString("price_format", comment: "Price display format")
        let priceMessage = String.localizedStringWithFormat(priceFormat, 99.99)
        print(priceMessage) // Output: "Price: $99.99" (or localized version)
        
        // Example with date formatting
        let dateFormat = NSLocalizedString("date_format", comment: "Date display format")
        let dateMessage = String.localizedStringWithFormat(dateFormat, "Monday", "January", 15)
        print(dateMessage) // Output: "Today is Monday, January 15" (or localized version)
        
        // Complex example with multiple parameters
        let complexFormat = NSLocalizedString("complex_message", comment: "Complex message with multiple parameters")
        let complexMessage = String.localizedStringWithFormat(complexFormat, "Alice", 3, "Bob")
        print(complexMessage) // Output: "Hello Alice, you have 3 messages from Bob" (or localized version)
    }
    
    // MARK: - SwiftUI Usage
    
    func swiftUIExamples() {
        // In SwiftUI, you can use Text with localization
        /*
        import SwiftUI
        
        struct ContentView: View {
            var body: some View {
                VStack {
                    Text("greeting")
                        .font(.title)
                    
                    Text("welcome_message", "John")
                        .font(.body)
                    
                    Text("item_count", 5)
                        .font(.caption)
                }
            }
        }
        */
    }
    
    // MARK: - UIKit Usage
    
    func uikitExamples() {
        // In UIKit, you can use localized strings in UI elements
        /*
        let alert = UIAlertController(
            title: NSLocalizedString("error", comment: "Error title"),
            message: NSLocalizedString("error_connect_desc", comment: "Connection error description"),
            preferredStyle: .alert
        )
        
        alert.addAction(UIAlertAction(
            title: NSLocalizedString("ok", comment: "OK button"),
            style: .default
        ))
        */
    }
    
    // MARK: - Advanced Usage with Custom Localization
    
    func advancedLocalizationExamples() {
        // You can also create custom localization functions
        func localizedString(_ key: String, arguments: CVarArg...) -> String {
            let format = NSLocalizedString(key, comment: "")
            return String.localizedStringWithFormat(format, arguments)
        }
        
        // Usage
        let message1 = localizedString("welcome_message", "Alice")
        let message2 = localizedString("item_count", 10)
        let message3 = localizedString("complex_message", "Bob", 5, "Charlie")
        
        print(message1)
        print(message2)
        print(message3)
    }
}

// MARK: - Project Setup Instructions

/*
To use the generated .xcstrings file in your Xcode project:

1. Add the Localizable.xcstrings file to your Xcode project
2. Make sure it's added to your app target
3. In your project settings, go to "Localizations" and add the languages you want to support
4. The .xcstrings file will automatically be used by NSLocalizedString

Project Structure:
MyApp/
├── Localizable.xcstrings (generated file)
├── Sources/
│   ├── ViewControllers/
│   ├── Views/
│   └── Models/
└── Resources/

Usage in Code:
- Use NSLocalizedString("key", comment: "comment") for simple strings
- Use String.localizedStringWithFormat for parameterized strings
- In SwiftUI, use Text("key", arguments...) for parameterized strings

Parameter Format Conversion:
- Flutter format: {name} → Xcode format: %@
- Android format: %1$s → Xcode format: %@
- Xcode format: %@, %1$@, %2$@ (where @ represents any object type)

Example conversions:
- "Welcome, {name}!" → "Welcome, %@!"
- "You have {count} items" → "You have %@ items"
- "Price: ${price}" → "Price: $%@"
*/
