#include <ArduinoJson.h>
#include <StreamUtils.h>

//Global and system wide variables 
int switchStateArray[10];
StaticJsonDocument<768> JSONdataOut;
// DynamicJsonDocument JSONdataOut(JSON_OBJECT_SIZE(20));
String serialJSONOut;

void setup() {
  // put your setup code here, to run once:

}

void loop() {
  StaticJsonDocument<768> doc;

  doc["Power"] = 10;
  doc["Left Door Command"] = 1;
  doc["Right Door Command"] = 1;
  doc["Service Brake Command"] = 1;
  doc["Emergency Brake Command"] = 1;
  doc["External Light Command"] = 1;
  doc["Internal Light Command"] = 1;
  doc["AC"] = 1;
  doc["Station Announcement"] = "text";
  doc["Engine State"] = 1;
  doc["Emergency Brake State"] = 1;
  doc["Service Brake State"] = 1;
  doc["Internal Lights State"] = 1;
  doc["External Lights State"] = 1;
  doc["Left Door State"] = 1;
  doc["Right Door State"] = 1;
  doc["Station"] = "text";
  doc["Current Speed"] = 10;
  doc["Commanded Speed"] = 10;
  doc["Authority"] = 10;
  doc["Speed Limit"] = 10;
  doc["Temperature"] = 10;
  doc["Communications Status"] = 1;

  serializeJson(doc, serialJSONOut);
}
