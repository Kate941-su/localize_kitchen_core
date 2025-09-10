# Localize Kitchen

A Python-based localization tool that generates platform-specific localization files from unified JSON source files. This tool supports multiple platforms including Android, Flutter, and Xcode, with automatic parameter format conversion.

## Features

- **Unified Source Format**: Use Android-style parameter format (`%1$s`, `%2$d`, `%1$.2f`) as the base format
- **Multi-Platform Support**: Generate localization files for Android, Flutter, and Xcode
- **Automatic Parameter Conversion**: Convert parameters to platform-specific formats
- **Batch Processing**: Process multiple languages simultaneously
- **Flexible Configuration**: Easy setup with builder pattern

## Supported Platforms

| Platform | Status | Output Format | Parameter Format |
|----------|--------|---------------|------------------|
| **Android** | ✅ Complete | XML (`strings.xml`) | `%1$s`, `%2$d`, `%1$.2f` |
| **Flutter** | ✅ Complete | ARB (`.arb`) | `{param1}`, `{param2}` |
| **React Native** | ✅ Complete | JavaScript (`.js`) | `{0}`, `{1}`, `{2}` |
| **Xcode** | 🚧 TODO | `.xcstrings` | `%@` |

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd localize_kitchen
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
localize_kitchen/
├── src/
│   ├── localize_creater/
│   │   ├── localize_creater.py      # Main localization logic
│   │   └── localize_creater_builder.py  # Builder pattern implementation
│   ├── locale_code/
│   │   └── code_list.py            # Supported language codes
│   └── sdk/
│       └── sdk.py                  # Supported SDKs
├── sample_data/                    # Input JSON files
│   ├── sample_en.json             # English (base language)
│   ├── sample_ja.json             # Japanese
│   ├── sample_ar.json             # Arabic
│   └── sample_de.json             # German
├── sample_output/                  # Generated localization files
│   ├── android/                   # Android XML files
│   ├── dart/                      # Flutter ARB files
│   ├── javascript/                # React Native JavaScript files
│   └── xcode/                     # Xcode .xcstrings files
├── main.py                        # Main entry point
└── requirements.txt               # Python dependencies
```

## Usage

### Basic Usage

```python
from src.localize_creater.localize_creater_builder import LocalizeCreaterBuilder

# Create a localize creater
localize_creater_builder = LocalizeCreaterBuilder()
localize_creater_builder.set_language_code_list(["ja", "ar", "de"])
localize_creater_builder.set_base_language_code("en")
localize_creater_builder.set_sdk("android_studio")  # or "flutter", "xcode"
localize_creater = localize_creater_builder.build()

# Generate localization files
localize_creater.create_android()  # or create_flutter(), create_xcode()
```

### Platform-Specific Examples

#### Android XML Generation
```python
localize_creater_builder.set_sdk("android_studio")
localize_creater = localize_creater_builder.build()
localize_creater.create_android()
```

**Output**: `sample_output/android/strings.xml` and `values-{lang}/strings.xml`

#### Flutter ARB Generation
```python
localize_creater_builder.set_sdk("flutter")
localize_creater = localize_creater_builder.build()
localize_creater.create_flutter()
```

**Output**: `sample_output/dart/app_{lang}.arb`

#### React Native JavaScript Generation
```python
localize_creater_builder.set_sdk("react")
localize_creater = localize_creater_builder.build()
localize_creater.create_react()
```

**Output**: `sample_output/javascript/LocalizedStrings.js`

#### Xcode .xcstrings Generation
```python
localize_creater_builder.set_sdk("xcode")
localize_creater = localize_creater_builder.build()
localize_creater.create_xcode()
```

**Output**: `sample_output/xcode/Localizable.xcstrings`

## Input Format

### Base JSON Structure

Create JSON files in `sample_data/` with the following structure:

```json
{
    "greeting": "Hello",
    "welcome_message": "Welcome, %1$s!",
    "item_count": "You have %1$d items",
    "price_format": "Price: $%1$.2f",
    "date_format": "Today is %1$s, %2$s %3$d",
    "complex_message": "Hello %1$s, you have %2$d messages from %3$s"
}
```

### Parameter Format

Use **Android-style parameters** as the base format:

| Type | Format | Example | Description |
|------|--------|---------|-------------|
| String | `%1$s`, `%2$s` | `"Welcome, %1$s!"` | String parameters |
| Integer | `%1$d`, `%2$d` | `"You have %1$d items"` | Integer parameters |
| Float | `%1$.2f`, `%2$.3f` | `"Price: $%1$.2f"` | Float with decimal places |

## Output Formats

### Android XML
```xml
<?xml version="1.0" ?>
<resources>
    <string name="greeting">Hello</string>
    <string name="welcome_message">Welcome, %1$s!</string>
    <string name="item_count">You have %1$d items</string>
    <string name="price_format">Price: $%1$.2f</string>
</resources>
```

### Flutter ARB
```json
{
  "@@locale": "en",
  "greeting": "Hello",
  "welcome_message": "Welcome, {param1}!",
  "item_count": "You have {param1} items",
  "price_format": "Price: ${param1}",
  "welcome_message@parameter": {
    "param1": "StringParam1"
  }
}
```

### React Native JavaScript
```javascript
import LocalizedStrings from 'react-native-localization';

let strings = new LocalizedStrings({
  "en": {
    greeting: "Hello",
    welcome_message: "Welcome, {0}!",
    item_count: "You have {0} items",
    price_format: "Price: ${0}"
  },
  "ja": {
    greeting: "こんにちは",
    welcome_message: "{0}さん、ようこそ！",
    item_count: "{0}個のアイテムがあります",
    price_format: "価格: {0}円"
  }
});

export default strings;
```

### Xcode .xcstrings
```json
{
  "sourceLanguage": "en",
  "strings": {
    "greeting": {
      "localizations": {
        "en": {
          "stringUnit": {
            "state": "translated",
            "value": "Hello"
          }
        },
        "ja": {
          "stringUnit": {
            "state": "translated",
            "value": "こんにちは"
          }
        }
      }
    }
  },
  "version": "1.0"
}
```

## Parameter Conversion

The tool automatically converts Android-style parameters to platform-specific formats:

| Platform | Conversion | Example |
|----------|------------|---------|
| **Android** | No conversion | `%1$s` → `%1$s` |
| **Flutter** | `%1$s` → `{param1}` | `"Welcome, %1$s!"` → `"Welcome, {param1}!"` |
| **React Native** | `%1$s` → `{0}` | `"Welcome, %1$s!"` → `"Welcome, {0}!"` |
| **Xcode** | `%1$s` → `%@` | `"Welcome, %1$s!"` → `"Welcome, %@!"` |

## Platform Integration

### Android Integration

1. Copy generated XML files to your Android project:
   ```
   app/src/main/res/values/strings.xml
   app/src/main/res/values-ja/strings.xml
   app/src/main/res/values-ar/strings.xml
   ```

2. Use in Java/Kotlin:
   ```java
   String greeting = getString(R.string.greeting);
   String welcome = getString(R.string.welcome_message, "John");
   String itemCount = getString(R.string.item_count, 5);
   ```

### Flutter Integration

1. Copy generated ARB files to your Flutter project:
   ```
   lib/l10n/app_en.arb
   lib/l10n/app_ja.arb
   ```

2. Configure `l10n.yaml`:
   ```yaml
   arb-dir: lib/l10n
   template-arb-file: app_en.arb
   output-localization-file: app_localizations.dart
   ```

3. Use in Dart:
   ```dart
   String greeting = AppLocalizations.of(context)!.greeting;
   String welcome = AppLocalizations.of(context)!.welcome_message('John');
   ```

### React Native Integration

1. Install react-native-localization:
   ```bash
   npm install react-native-localization
   # or
   yarn add react-native-localization
   ```

2. Copy generated `LocalizedStrings.js` file to your React Native project

3. Use in your React Native components:
   ```javascript
   import strings from './LocalizedStrings';
   
   // Simple strings
   const greeting = strings.greeting;
   
   // Parameterized strings
   const welcome = strings.formatString(strings.welcome_message, ['John']);
   const itemCount = strings.formatString(strings.item_count, [5]);
   ```

4. In JSX:
   ```jsx
   <Text>{strings.greeting}</Text>
   <Text>{strings.formatString(strings.welcome_message, ['John'])}</Text>
   ```

### Xcode Integration

1. Copy generated `.xcstrings` file to your Xcode project
2. Add to your app target
3. Configure localizations in project settings
4. Use in Swift:
   ```swift
   let greeting = NSLocalizedString("greeting", comment: "Greeting message")
   let welcome = String.localizedStringWithFormat(
       NSLocalizedString("welcome_message", comment: ""), 
       "John"
   )
   ```

## Supported Languages

The tool supports standard language codes:

- `en` - English
- `ja` - Japanese
- `ar` - Arabic
- `de` - German
- `fr` - French
- `es` - Spanish
- `zh` - Chinese
- And more...

## Supported SDKs

- `android_studio` - Android development
- `flutter` - Flutter development
- `react` - React Native development
- `xcode` - iOS/macOS development

## Development Status

### ✅ Completed Features

- [x] Android XML generation
- [x] Flutter ARB generation
- [x] React Native JavaScript generation
- [x] Parameter format conversion
- [x] Multi-language support
- [x] Builder pattern implementation
- [x] Unified source format

### 🚧 TODO Features

- [ ] **Xcode .xcstrings generation** - Currently in development
- [ ] **Web platform support** - Planned for future release
- [ ] **CLI interface** - Command-line tool for easier usage
- [ ] **Batch processing** - Process multiple projects at once
- [ ] **Translation validation** - Check for missing translations
- [ ] **Parameter validation** - Validate parameter consistency across languages

### 🔄 In Progress

- [ ] **Xcode Integration** - Working on complete .xcstrings support
- [ ] **Documentation** - Expanding usage examples and best practices

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature/new-feature`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For questions, issues, or contributions, please:

1. Check the existing issues on GitHub
2. Create a new issue with detailed information
3. Contact the maintainers

## Changelog

### Version 1.0.0
- Initial release
- Android XML generation
- Flutter ARB generation
- React Native JavaScript generation
- Parameter format conversion
- Multi-language support

### Version 1.1.0 (Planned)
- Complete Xcode .xcstrings support
- CLI interface
- Enhanced documentation

---

**Note**: Xcode features are currently marked as TODO and are under active development. The current implementation provides basic .xcstrings generation, but full integration and testing are still in progress.
