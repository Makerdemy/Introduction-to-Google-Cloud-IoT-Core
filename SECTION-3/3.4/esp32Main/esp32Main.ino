#include "esp32-mqtt.h"

void setup() {
  // put your setup code here, to run once:
  Serial.begin(2000000);
  pinMode(LED_BUILTIN, OUTPUT);
  setupCloudIoT();
}

void loop() {
  mqttClient->loop();
  delay(10);  // <- fixes some issues with WiFi stability

  if (!mqttClient->connected()) {
    connect();
  }
}
