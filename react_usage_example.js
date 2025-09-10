// React Native Usage Example for LocalizedStrings
// This file demonstrates how to use the generated LocalizedStrings.js file

import React, { Component } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import strings from './LocalizedStrings';

class LocalizationExample extends Component {
  render() {
    return (
      <View style={styles.container}>
        {/* Simple strings */}
        <Text style={styles.title}>{strings.greeting}</Text>
        
        {/* Parameterized strings using formatString */}
        <Text style={styles.text}>
          {strings.formatString(strings.welcome_message, ['John'])}
        </Text>
        
        <Text style={styles.text}>
          {strings.formatString(strings.item_count, [5])}
        </Text>
        
        <Text style={styles.text}>
          {strings.formatString(strings.price_format, [99.99])}
        </Text>
        
        <Text style={styles.text}>
          {strings.formatString(strings.date_format, ['Monday', 'January', 15])}
        </Text>
        
        <Text style={styles.text}>
          {strings.formatString(strings.complex_message, ['Alice', 3, 'Bob'])}
        </Text>
      </View>
    );
  }
}

// Alternative usage with functional components
const FunctionalExample = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>{strings.greeting}</Text>
      <Text style={styles.text}>
        {strings.formatString(strings.welcome_message, ['Jane'])}
      </Text>
    </View>
  );
};

// Usage in different scenarios
class AdvancedExample extends Component {
  constructor(props) {
    super(props);
    this.state = {
      userName: 'Alice',
      itemCount: 10,
      price: 29.99
    };
  }

  render() {
    const { userName, itemCount, price } = this.state;
    
    return (
      <View style={styles.container}>
        {/* Dynamic content */}
        <Text style={styles.text}>
          {strings.formatString(strings.welcome_message, [userName])}
        </Text>
        
        <Text style={styles.text}>
          {strings.formatString(strings.item_count, [itemCount])}
        </Text>
        
        <Text style={styles.text}>
          {strings.formatString(strings.price_format, [price])}
        </Text>
        
        {/* Complex message with multiple parameters */}
        <Text style={styles.text}>
          {strings.formatString(strings.complex_message, [userName, itemCount, 'System'])}
        </Text>
      </View>
    );
  }
}

// Usage in navigation or other contexts
const NavigationExample = ({ navigation }) => {
  const userName = navigation.getParam('userName', 'Guest');
  
  return (
    <View style={styles.container}>
      <Text style={styles.title}>
        {strings.formatString(strings.welcome_message, [userName])}
      </Text>
    </View>
  );
};

// Usage with conditional rendering
const ConditionalExample = ({ isLoggedIn, userName }) => {
  return (
    <View style={styles.container}>
      {isLoggedIn ? (
        <Text style={styles.text}>
          {strings.formatString(strings.welcome_message, [userName])}
        </Text>
      ) : (
        <Text style={styles.text}>{strings.greeting}</Text>
      )}
    </View>
  );
};

// Usage in alerts or modals
const AlertExample = () => {
  const showAlert = () => {
    Alert.alert(
      strings.greeting,
      strings.formatString(strings.welcome_message, ['User']),
      [{ text: 'OK' }]
    );
  };

  return (
    <View style={styles.container}>
      <Button title="Show Alert" onPress={showAlert} />
    </View>
  );
};

// Usage with arrays and loops
const ListExample = () => {
  const items = ['bread', 'butter', 'milk'];
  
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Shopping List</Text>
      {items.map((item, index) => (
        <Text key={index} style={styles.text}>
          {strings.formatString(strings.item_count, [index + 1])}: {item}
        </Text>
      ))}
    </View>
  );
};

// Styles
const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#fff',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    textAlign: 'center',
  },
  text: {
    fontSize: 16,
    marginBottom: 10,
    lineHeight: 24,
  },
});

export default LocalizationExample;

// Additional usage patterns:

// 1. Setting language programmatically
// strings.setLanguage('ja'); // Switch to Japanese
// strings.setLanguage('en'); // Switch to English

// 2. Getting current language
// const currentLanguage = strings.getLanguage();

// 3. Getting available languages
// const availableLanguages = strings.getAvailableLanguages();

// 4. Usage in Redux or Context
// const LocalizationContext = React.createContext(strings);

// 5. Usage with hooks (React Native 0.59+)
// const useLocalization = () => {
//   const [language, setLanguage] = useState(strings.getLanguage());
//   
//   const changeLanguage = (lang) => {
//     strings.setLanguage(lang);
//     setLanguage(lang);
//   };
//   
//   return { language, changeLanguage, strings };
// };

// 6. Usage in API calls or async operations
// const fetchUserData = async (userId) => {
//   try {
//     const response = await api.getUser(userId);
//     const welcomeMessage = strings.formatString(
//       strings.welcome_message, 
//       [response.data.name]
//     );
//     return welcomeMessage;
//   } catch (error) {
//     return strings.greeting; // Fallback message
//   }
// };

// 7. Usage with date formatting
// import { format } from 'date-fns';
// 
// const DateExample = () => {
//   const today = new Date();
//   const formattedDate = format(today, 'EEEE, MMMM do');
//   
//   return (
//     <Text>
//       {strings.formatString(strings.date_format, [
//         format(today, 'EEEE'), // Day name
//         format(today, 'MMMM'), // Month name
//         today.getDate()        // Day number
//       ])}
//     </Text>
//   );
// };
