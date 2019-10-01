// This file contains static methods for API requests using Wifi / MQTT
#ifndef __ESP32_MQTT_H__
#define __ESP32_MQTT_H__

#include <Client.h>
#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <LiquidCrystal_I2C.h>

#include <MQTT.h>

#include <CloudIoTCore.h>
#include <CloudIoTCoreMqtt.h>
#include "ciotc_config.h" // Update this file with your configuration

int lcdColumns = 16;
int lcdRows = 2;
byte address =  //<!Use your LCD display's address>;, Example : 0x3F;

LiquidCrystal_I2C lcd(address, lcdColumns, lcdRows);

// The MQTT callback function for commands and configuration updates
// Place your message handler code here.
void messageReceived(String &topic, String &payload) {
  Serial.println("incoming: " + topic + " - " + payload);
  int ledonpos=payload.indexOf("ledon");
  if (ledonpos != -1) {
    // If yes, switch ON the ESP32 internal led
    Serial.println("Switch led on");
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Limit Crossed");
    digitalWrite(LED_BUILTIN, HIGH);
  } else {
    // If no, switch off the ESP32 internal led
    Serial.println("Switch led off");
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Safe limit");    
    digitalWrite(LED_BUILTIN, LOW);
  }  
}  

/////////////////////////////////////////////
// Initialize WiFi and MQTT for this board //
Client *netClient;
CloudIoTCoreDevice *device;
CloudIoTCoreMqtt *mqtt;
MQTTClient *mqttClient;
unsigned long iss = 0;
String jwt;

/*
///////////////////////////////
// Helpers specific to this board
///////////////////////////////
String getDefaultSensor() {
  return  "Wifi: " + String(WiFi.RSSI()) + "db";
}
*/

String getJwt() {
  iss = time(nullptr);
  Serial.println("Refreshing JWT");
  jwt = device->createJWT(iss, jwt_exp_secs);
  return jwt;
}

void setupWifi() {
  Serial.println("Starting wifi");

  WiFi.mode(WIFI_STA);
  // WiFi.setSleep(false); // May help with disconnect? Seems to have been removed from WiFi
  WiFi.begin(ssid, password);
  Serial.println("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(100);
  }

  configTime(0, 0, ntp_primary, ntp_secondary);
  Serial.println("Waiting on time sync...");
  while (time(nullptr) < 1510644967) {
    delay(10);
  }
}

void connectWifi() {
  Serial.print("checking wifi...");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(1000);
  }
}

void connect() {
  connectWifi();
  mqtt->mqttConnect();
}

void setupCloudIoT() {
  device = new CloudIoTCoreDevice(
      project_id, location, registry_id, device_id,
      private_key_str);

  setupWifi();
  netClient = new WiFiClientSecure();
  mqttClient = new MQTTClient(512);
  mqttClient->setOptions(180, true, 1000); // keepAlive, cleanSession, timeout
  mqtt = new CloudIoTCoreMqtt(mqttClient, netClient, device);
  mqtt->setUseLts(true);
  mqtt->startMQTT();
}
#endif //__ESP32_MQTT_H__
