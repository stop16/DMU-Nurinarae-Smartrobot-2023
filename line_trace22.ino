#include<PRIZM.h>
PRIZM prizm;
EXPANSION exc;

String sig = "";
int funcflag = 0;
int count = 0;

void wheel(int x, int y, int z) // Omni wheel 이동공식
{
  int A = 0, B = 0, C = 0, D = 0;

  A = (x * 0.5) + (y * 0.5) + (z * 0.841471);
  B = (x * 0.5 * -1) + (y * 0.5) + (z * 0.841471);
  C = (x * 0.5 * -1) + (y * 0.5 * -1) + (z * 0.841471);
  D = (x * 0.5) + (y * 0.5 * -1) + (z * 0.841471);
  exc.setMotorSpeeds(1, A, B);
  exc.setMotorSpeeds(2, C, D);
}

void line()
{

  while (1)
  {
    if (digitalRead(2) == 1 && digitalRead(3) == 1 && digitalRead(4) == 1)
    {
      wheel(0, 0, 0);
      break;
    }
    if (digitalRead(2) == 1 && digitalRead(3) == 0 && digitalRead(4) == 0)
    {
      wheel(0, -80, 150);
    }
    if (digitalRead(2) == 0 && digitalRead(3) == 0 && digitalRead(4) == 1)
    {
      wheel(0, 80, 150);
    }
    else
    {
      wheel(-50, 0, 250);
    }
  }
  funcflag = 0;
}

/*
void line()
{
  while (1)
  {
    int sensor2 = digitalRead(2);
    int sensor3 = digitalRead(3);
    int sensor4 = digitalRead(4);

    if (sensor2 == 1 && sensor3 == 1 && sensor4 == 1)
    {
      wheel(0, 380, 0);
    }
    if (sensor2 == 0 && sensor3 == 0 && sensor4 == 0)
    {
      wheel(0, 0, 0);
      break;
    }
    if (sensor2 == 0 && sensor3 == 1 && sensor4 == 0)
    {
      wheel(0, 380, 0);
    }
    if (sensor2 == 0 && sensor3 == 0 && sensor4 == 1)
    {
       wheel(0, 380, 20);
    }
    if (sensor2 == 1 && sensor3 == 0 && sensor4 == 0)
    {
      wheel(0, 380, -20);      
    }
  }
  funcflag = 0;
}
*/
/*
void line()
{
  while (1)
  {
    if (digitalRead(2) == 1 && digitalRead(3) == 1 && digitalRead(4) == 1)
    {
      // Serial.print(33);
      Serial.println("1");
      wheel(0, 0, 0);
      break;
    }
    if (digitalRead(2) == 1 && digitalRead(3) == 1 && digitalRead(4) == 0)
    {
      Serial.println("2");
      wheel(0, 300, 100);
    }
    if (digitalRead(2) == 1 && digitalRead(3) == 0 && digitalRead(4) == 1)
    {
      Serial.println("3");
      wheel(0, 300, 0);
    }
    if (digitalRead(2) == 0 && digitalRead(3) == 1 && digitalRead(4) == 1)
    {
      Serial.println("5");
      wheel(0, 300, -100);
    }
    if (digitalRead(2) == 0 && digitalRead(3) == 1 && digitalRead(4) == 0)
    {
      Serial.println("7");
      // Serial.print(digitalRead(3));
      wheel(0, 300, 0);
      if (digitalRead(2) == 0 && digitalRead(3) == 0 && digitalRead(4) == 0)
      {
        Serial.println("8");
        wheel(0, 300, 0);
      }
    }
  }
}
*/
void opening()
{
  while (1) {
    exc.setMotorSpeeds(1, -200, 200);
    exc.setMotorSpeeds(2, -200, 200);
    if (digitalRead(4) == 1)
    {
      exc.setMotorSpeeds(1, 0, 0);
      exc.setMotorSpeeds(2, 0, 0);
      break;
    }
  }
  while (1) {
    exc.setMotorSpeeds(1, 160, 160);
    exc.setMotorSpeeds(2, 160, 160);
    if (digitalRead(2) == 1 && digitalRead(3) == 1 && digitalRead(4) == 1)
    {
      exc.setMotorSpeeds(1, 0, 0);
      exc.setMotorSpeeds(2, 0, 0);
      break;
    }
  }
  
  exc.resetEncoders(1);
  exc.resetEncoders(2);
  exc.setMotorTargets(1, 100, 180, 100, 180);
  exc.setMotorTargets(2, 100, 180, 100, 180);
  while (exc.readMotorBusy(1, 1)) {}
  while (1)
  {
    exc.setMotorSpeeds(1, -80, 80);
    exc.setMotorSpeeds(2, -80, 80);
    if (digitalRead(3) == 1)
    {
      exc.setMotorSpeeds(1, 0, 0);
      exc.setMotorSpeeds(2, 0, 0);
      break;
    }
  }
  funcflag = 0;
}

void Go()
{
  wheel(0, 200, 0);
}

void Stop()
{
  wheel(0, 0, 0);
}

int sendflag = 0;
char tmpcmd;

char command;

void setup() {
  prizm.PrizmBegin();
  exc.setMotorInvert(2, 1, 1);
  exc.setMotorInvert(2, 2, 1);
  Serial.setTimeout(10);
  Serial.begin(9600);
  while (1)
  {
    Serial.println('k');
    delay(500);
    command = Serial.read();
    if (command == 'p')
    {
      break;
    }
  }
  Serial.flush();
}


void loop() {
  if (Serial.available())
  {
    command = Serial.read();
  }
  
  if (command == 'o')
  {
    funcflag = 1;
    opening();
    while(funcflag == 1){}
    Serial.println(command);
    command = 0;
  }
  
  if (command == 'x')
  {
    Stop();
  }
  if (command == 'f')
  {
    funcflag = 1;
    line();
    while(funcflag == 1){}
    Serial.println(command);
    command = 0;
  }
}
