#include <LiquidCrystal_I2C.h>

// set the LCD number of columns and rows
int lcdColumns = 16;
int lcdRows = 2;

// Uncomment this line and assign the address you got from I2C scanner sketch
//byte address = <PUT YOUR ADDRESS HERE> //0x3F;

// set LCD address, number of columns and rows
// if you don't know your display address, run an I2C scanner sketch
LiquidCrystal_I2C lcd(address, lcdColumns, lcdRows);  

void setup(){
  // initialize LCD
  lcd.init();
  // turn on LCD backlight                      
  lcd.backlight();
}

void loop(){
  // set cursor to first column, first row
  lcd.setCursor(0, 0);
  // print message
  lcd.print("Hello there!");
  // Wait one second  
  delay(1000);
  // clears the display to print new message
  lcd.clear();
  // set cursor to first column, first row
  lcd.setCursor(0, 0);
  lcd.print("You finshed 3.2");
  // set cursor to seventh column, second row  
  lcd.setCursor(7,1);
  lcd.print(":)");  
  delay(1000);
  lcd.clear(); 
}
