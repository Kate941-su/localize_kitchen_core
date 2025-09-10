// Android Usage Example for Parameterized Strings
// This file demonstrates how to use the generated XML string resources with parameters

package com.example.localizationdemo;

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;
import java.util.Locale;

public class MainActivity extends Activity {
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        // Get string resources
        String greeting = getString(R.string.greeting);
        
        // Parameterized strings examples
        String welcomeMessage = getString(R.string.welcome_message, "John");
        String itemCount = getString(R.string.item_count, 5);
        String priceFormat = getString(R.string.price_format, 99.99);
        String dateFormat = getString(R.string.date_format, "Monday", "January", 15);
        String complexMessage = getString(R.string.complex_message, "Alice", 3, "Bob");
        
        // Display the strings
        displayStrings(greeting, welcomeMessage, itemCount, priceFormat, dateFormat, complexMessage);
    }
    
    private void displayStrings(String greeting, String welcome, String items, 
                               String price, String date, String complex) {
        // Example of how to use the strings in your UI
        TextView greetingView = findViewById(R.id.greeting_text);
        greetingView.setText(greeting);
        
        TextView welcomeView = findViewById(R.id.welcome_text);
        welcomeView.setText(welcome);
        
        TextView itemsView = findViewById(R.id.items_text);
        itemsView.setText(items);
        
        TextView priceView = findViewById(R.id.price_text);
        priceView.setText(price);
        
        TextView dateView = findViewById(R.id.date_text);
        dateView.setText(date);
        
        TextView complexView = findViewById(R.id.complex_text);
        complexView.setText(complex);
    }
}

// Alternative usage with different parameter types:
class StringResourceExamples {
    
    public void demonstrateParameterTypes(Activity activity) {
        // String parameters (%1$s, %2$s, etc.)
        String name = "John";
        String message = activity.getString(R.string.welcome_message, name);
        
        // Integer parameters (%1$d, %2$d, etc.)
        int count = 5;
        String itemText = activity.getString(R.string.item_count, count);
        
        // Float parameters (%1$.2f, %2$.3f, etc.)
        float price = 99.99f;
        String priceText = activity.getString(R.string.price_format, price);
        
        // Mixed parameters
        String day = "Monday";
        String month = "January";
        int date = 15;
        String dateText = activity.getString(R.string.date_format, day, month, date);
        
        // Complex example with multiple parameters
        String userName = "Alice";
        int messageCount = 3;
        String sender = "Bob";
        String complexText = activity.getString(R.string.complex_message, userName, messageCount, sender);
    }
}

// XML Layout Example (activity_main.xml):
/*
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp">

    <TextView
        android:id="@+id/greeting_text"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textSize="24sp"
        android:textStyle="bold" />

    <TextView
        android:id="@+id/welcome_text"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="16dp" />

    <TextView
        android:id="@+id/items_text"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="8dp" />

    <TextView
        android:id="@+id/price_text"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="8dp" />

    <TextView
        android:id="@+id/date_text"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="8dp" />

    <TextView
        android:id="@+id/complex_text"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="8dp" />

</LinearLayout>
*/

// Android Parameter Format Reference:
/*
%[argument_index$][flags][width][.precision]conversion

Common conversions:
- %s = String
- %d = Integer
- %f = Float
- %c = Character
- %b = Boolean

Examples:
- %1$s = First argument as String
- %2$d = Second argument as Integer
- %1$.2f = First argument as Float with 2 decimal places
- %3$s = Third argument as String

Parameter order can be different from argument order:
- "Hello %2$s, you have %1$d items" with args (5, "John") = "Hello John, you have 5 items"
*/
