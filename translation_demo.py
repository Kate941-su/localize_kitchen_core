#!/usr/bin/env python3
"""
Demo script showing how to use the translated JSON files
"""
import orjson
import os

def load_translations():
    """Load all translation files"""
    translations = {}
    
    # List of available languages
    languages = ['en', 'de', 'ar', 'ja']
    
    for lang in languages:
        file_path = f"sample_data/sample_{lang}.json"
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                translations[lang] = orjson.loads(f.read())
                print(f"✅ Loaded {lang.upper()} translations")
        else:
            print(f"❌ File not found: {file_path}")
    
    return translations

def display_translations(translations):
    """Display translations in a nice format"""
    print("\n" + "="*60)
    print("TRANSLATION COMPARISON")
    print("="*60)
    
    # Get all keys from the first language
    if not translations:
        print("No translations loaded!")
        return
    
    first_lang = list(translations.keys())[0]
    keys = list(translations[first_lang].keys())
    
    # Display header
    header = f"{'Key':<15}"
    for lang in translations.keys():
        header += f"{lang.upper():<15}"
    print(header)
    print("-" * (15 * (len(translations) + 1)))
    
    # Display translations
    for key in keys:
        row = f"{key:<15}"
        for lang in translations.keys():
            if key in translations[lang]:
                row += f"{translations[lang][key]:<15}"
            else:
                row += f"{'N/A':<15}"
        print(row)

def interactive_translator(translations):
    """Interactive translation lookup"""
    print("\n" + "="*60)
    print("INTERACTIVE TRANSLATOR")
    print("="*60)
    print("Available languages:", ", ".join(translations.keys()))
    print("Type 'quit' to exit")
    
    while True:
        key = input("\nEnter a key to translate: ").strip()
        if key.lower() == 'quit':
            break
        
        if not key:
            continue
            
        print(f"\nTranslations for '{key}':")
        print("-" * 30)
        
        found = False
        for lang, data in translations.items():
            if key in data:
                print(f"{lang.upper():<5}: {data[key]}")
                found = True
        
        if not found:
            print("Key not found in any translation file!")
            print("Available keys:", ", ".join(list(translations.values())[0].keys()))

def main():
    """Main function"""
    print("🌍 Localization Kitchen - Translation Demo")
    print("="*50)
    
    # Load translations
    translations = load_translations()
    
    if not translations:
        print("❌ No translation files found!")
        return
    
    # Display all translations
    display_translations(translations)
    
    # Interactive mode
    interactive_translator(translations)
    
    print("\n👋 Thank you for using Localization Kitchen!")

if __name__ == "__main__":
    main()

