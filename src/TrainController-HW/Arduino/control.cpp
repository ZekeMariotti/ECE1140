int previousError = 0;
int previousU = 0; 

int calculatePower(int currentSpeed, int commandedSpeed, int currentTime, int PreviousTime, float dt){
  //power calculation here
  int Kp = 1;
  int Ki = 1;
  int error = commandedSpeed - currentSpeed;

  int power = Kp*error + Ki*(previousU + (dt/2)*(error-previousError));
  previousU = (dt/2)*(error-previousError);
  previousError = error;

  return power;

}

void automaticSpeedControl(){

}

void calculateBrake(bool state){
  return state;
}

