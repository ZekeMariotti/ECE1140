#define __ASSERT_USE_STDERR

#include <assert.h>

int x =3;

void setup() {
  // put your setup code here, to run once:
  // initialize serial communication at 9600 bits per second.
    Serial.begin(9600);  
}

void loop() {
  // put your main code here, to run repeatedly:
  assert(x==3);
  Serial.println("Test Passed");
  delay(500);
  abort();

}


// handle diagnostic informations given by assertion and abort program execution:
void __assert(const char *__func, const char *__file, int __lineno, const char *__sexp) {
    // transmit diagnostic informations through serial link. 
    Serial.println(__func);
    Serial.println(__file);
    Serial.println(__lineno, DEC);
    Serial.println(__sexp);
    Serial.println("Test Failed");
    Serial.flush();
    // abort program execution.
    abort();
}