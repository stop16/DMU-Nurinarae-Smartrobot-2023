#include<PRIZM.h>

#define L 2
#define R 1

PRIZM prizm;
EXPANSION exc;

int funcflag = 0;
int count = 0;
int sendflag = 0;
char tmpcmd;
char command;
int bf;

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

void mov()
{
  exc.resetEncoders(1);
  exc.resetEncoders(2);
  exc.setMotorTargets(L, 90, 285, 90, 285);
  exc.setMotorTargets(R, 70, 285, 70, 285);
  while (exc.readMotorBusy(1, 1)) {}
}

void movv()
{
  wheel(0, 0, 240);
  delay(200);
}

void line()
{
  while (1)
  {
    if (digitalRead(2) == 1 && digitalRead(3) == 1 && digitalRead(4) == 1)
    {
      break;
    }
    else if (digitalRead(2) == 1 && digitalRead(3) == 0 && digitalRead(4) == 0)
    {
      exc.setMotorSpeeds(L, -90, -90);
      exc.setMotorSpeeds(R, 70, 70);

    }
    else if (digitalRead(2) == 0 && digitalRead(3) == 0 && digitalRead(4) == 1)
    {

      exc.setMotorSpeeds(L, 90, 90);
      exc.setMotorSpeeds(R, -70, -70);
      delay(5);

    }
    else
    {
      exc.setMotorSpeeds(L, 90, 90);
      exc.setMotorSpeeds(R, 70, 70);
    }
  }
  exc.setMotorSpeeds(L, 0, 0);
  exc.setMotorSpeeds(R, 0, 0);
  mov();
  funcflag = 0;
}

/*
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
      wheel(0, -60, 150);
    }
    if (digitalRead(2) == 0 && digitalRead(3) == 0 && digitalRead(4) == 1)
    {
      wheel(0, 60, 150);
    }
    else
    {
      wheel(-50, 0, 250);
    }
  }
  mov();
  funcflag = 0;
  }
*/
void opening()
{
  while (1) {
    exc.setMotorSpeeds(L, -60, 60);
    exc.setMotorSpeeds(R, -60, 60);
    if (digitalRead(4) == 1)
    {
      exc.setMotorSpeeds(1, 0, 0);
      exc.setMotorSpeeds(2, 0, 0);
      break;
    }
  }
  while (1) {
    exc.setMotorSpeeds(L, 60, 60);
    exc.setMotorSpeeds(R, 60, 60);
    if (digitalRead(2) == 1 && digitalRead(3) == 1 && digitalRead(4) == 1)
    {
      exc.setMotorSpeeds(1, 0, 0);
      exc.setMotorSpeeds(2, 0, 0);
      break;
    }
  }

  exc.resetEncoders(1);
  exc.resetEncoders(2);
  exc.setMotorTargets(L, 70, 180, 70, 180);
  exc.setMotorTargets(R, 70, 180, 70, 180);
  while (exc.readMotorBusy(1, 1)) {}
  while (1)
  {
    exc.setMotorSpeeds(L, -80, 80);
    exc.setMotorSpeeds(R, -80, 80);
    if (digitalRead(3) == 1)
    {
      exc.setMotorSpeeds(1, 0, 0);
      exc.setMotorSpeeds(2, 0, 0);
      break;
    }
  }
  funcflag = 0;
}

void ending()
{
  line(); // 마동지막 칸 까지 이
  //마지막 세개 인식 이후 동작임
  exc.resetEncoders(1);
  exc.resetEncoders(2);
  exc.setMotorTargets(L, 150, 720, -150, -720);
  exc.setMotorTargets(R, 150, 720, -150, -720);
  while (exc.readMotorBusy(1, 1)) {}
  exc.resetEncoders(1);
  exc.resetEncoders(2);
  exc.setMotorTargets(L, 150, 1240, 150, 1240);
  exc.setMotorTargets(R, 150, 1240, 150, 1240);
  while (exc.readMotorBusy(1, 1)) {}
  funcflag = 0;
}

void line_s()
{
  while (1)
  {
    if (digitalRead(2) == 1 && digitalRead(3) == 1 && digitalRead(4) == 1)
    {
      exc.setMotorSpeeds(1, 0, 0);
      exc.setMotorSpeeds(2, 0, 0);
      break;
    }
    else if (digitalRead(2) == 1 && digitalRead(3) == 0 && digitalRead(4) == 0)
    {
      exc.setMotorSpeeds(L, -40, -40);
      exc.setMotorSpeeds(R, 40, 40);
    }
    else if (digitalRead(2) == 0 && digitalRead(3) == 0 && digitalRead(4) == 1)
    {
      exc.setMotorSpeeds(L, 40, 40);
      exc.setMotorSpeeds(R, -40, -40);
      delay(5);
    }
    else
    {
      exc.setMotorSpeeds(L, 40, 40);
      exc.setMotorSpeeds(R, 40, 40);
    }
  }
  mov();
  funcflag = 0;
}

void left()
{
  exc.setMotorSpeeds(L, -80, -80);
  exc.setMotorSpeeds(R, 80, 80);
  delay(400);
  while (1) {
    exc.setMotorSpeeds(L, -80, -80);
    exc.setMotorSpeeds(R, 80, 80);
    if (digitalRead(2) == 0 && digitalRead(3) == 1) {
      exc.setMotorSpeeds(1, 0, 0);
      exc.setMotorSpeeds(2, 0, 0);
      break;
    }
  }
  exc.setMotorSpeeds(L, -80, -80);
  exc.setMotorSpeeds(R, 80, 80);
  delay(90);
  exc.setMotorSpeeds(L, 0, 0);
  exc.setMotorSpeeds(R, 0, 0);
  funcflag = 0;
}

void left_s()
{

  while (1) {
    exc.setMotorSpeeds(L, -60, -60);
    exc.setMotorSpeeds(R, 60, 60);
    delay(5);
    if (digitalRead(3) == 1) {
      exc.setMotorSpeeds(1, 0, 0);
      exc.setMotorSpeeds(2, 0, 0);
      break;
    }
  }
}

void right()
{
  exc.setMotorSpeeds(L, 80, 80);
  exc.setMotorSpeeds(R, -80, -80);
  delay(400);
  while (1) {
    exc.setMotorSpeeds(L, 80, 80);
    exc.setMotorSpeeds(R, -80, -80);
    if (digitalRead(4) == 0 && digitalRead(3) == 1) {
      exc.setMotorSpeeds(1, 0, 0);
      exc.setMotorSpeeds(2, 0, 0);
      break;
    }

  }
  exc.setMotorSpeeds(L, 80, 80);
  exc.setMotorSpeeds(R, -80, -80);
  delay(90);
  exc.setMotorSpeeds(1, 0, 0);
  exc.setMotorSpeeds(2, 0, 0);
  funcflag = 0;
}

void right_s()
{
  while (1) {
    exc.setMotorSpeeds(L, 60, 60);
    exc.setMotorSpeeds(R, -60, -60);
    delay(5);
    if (digitalRead(3) == 1) {
      exc.setMotorSpeeds(1, 0, 0);
      exc.setMotorSpeeds(2, 0, 0);
      break;
    }
  }
  funcflag = 0;
}

void grip_left()
{
  right();
  exc.resetEncoders(1);
  exc.resetEncoders(2);
  exc.setMotorTargets(1, 160, 90, 160, 90);
  exc.setMotorTargets(2, 160, 90, 160, 90);
  while (exc.readMotorBusy(1, 1)) {}
  right();
  right();
  delay(300);
  left_s();
  funcflag = 0;
}

void grip_right()
{
  left();
  exc.resetEncoders(1);
  exc.resetEncoders(2);
  exc.setMotorTargets(1, 160, 90, 160, 90);
  exc.setMotorTargets(2, 160, 90, 160, 90);
  while (exc.readMotorBusy(1, 1)) {}
  left();
  left();
  delay(300);
  right_s();
  funcflag = 0;
}

void grip_open_1()
{
  /*
    exc.resetEncoders(1);
    exc.resetEncoders(2);
    exc.setMotorTargets(1, -40, -30, -40, -30);
    exc.setMotorTargets(2, -40, -30, -40, -30);
    while (exc.readMotorBusy(1, 1)) {}
  */
  bf = 1;
  delay(200);
  prizm.setServoPosition(1, 150);
  prizm.setServoPosition(2, 35);
  delay(1000);
}

void grip_close_1()
{
  delay(200);
  prizm.setServoPosition(1, 85);
  prizm.setServoPosition(2, 100);
  delay(1000);
}

void grip_open_2()
{
  /*
    exc.resetEncoders(1);
    exc.resetEncoders(2);
    exc.setMotorTargets(1, -40, -30, -40, -30);
    exc.setMotorTargets(2, -40, -30, -40, -30);
    while (exc.readMotorBusy(1, 1)) {}
  */
  bf = 1;
  delay(200);
  prizm.setServoPosition(3, 155);
  prizm.setServoPosition(4, 25);
  delay(1000);
}

void grip_close_2()
{
  delay(200);
  prizm.setServoPosition(3, 98);
  prizm.setServoPosition(4, 82);
  delay(1000);
}

void grip_open_3()
{
  /*
    exc.resetEncoders(1);
    exc.resetEncoders(2);
    exc.setMotorTargets(1, -40, -30, -40, -30);
    exc.setMotorTargets(2, -40, -30, -40, -30);
    while (exc.readMotorBusy(1, 1)) {}
  */
  bf = 1;
  delay(200);
  prizm.setServoPosition(5, 152);
  prizm.setServoPosition(6, 35);
  delay(1000);
}

void grip_close_3()
{
  delay(200);
  prizm.setServoPosition(5, 87);
  prizm.setServoPosition(6, 100);
  delay(1000);
}

void cube_in()
{
  while (digitalRead(5) == 1)
  {
    if (digitalRead(2) == 1 && digitalRead(3) == 0 && digitalRead(4) == 0)
    {
      while (1)
      {
        exc.setMotorSpeeds(L, -15, -15);
        exc.setMotorSpeeds(R, 15, 15);
        if (digitalRead(2) == 0 && digitalRead(3) == 1 && digitalRead(4) == 0)
        {
          break;
        }
      }
    }
    if (digitalRead(2) == 0 && digitalRead(3) == 0 && digitalRead(4) == 1)
    {
      while (1)
      {
        exc.setMotorSpeeds(L, 15, 15);
        exc.setMotorSpeeds(R, -15, -15);
        delay(5);
        if (digitalRead(2) == 0 && digitalRead(3) == 1 && digitalRead(4) == 0)
        {
          break;
        }
      }
    }
    else
    {
      exc.setMotorSpeeds(L, 15, 15);
      exc.setMotorSpeeds(R, 15, 15);
    }
  }
  exc.setMotorSpeeds(1, 0, 0);
  exc.setMotorSpeeds(2, 0, 0);
}

void cube_out()
{
  exc.resetEncoders(1);
  exc.resetEncoders(2);
  exc.setMotorTargets(L, -80, -120, -80, -120);
  exc.setMotorTargets(R, -80, -120, -80, -120);
  while (exc.readMotorBusy(1, 1)) {}
}

void macro_close_1()
{
  prizm.setServoPosition(1, 150);
  prizm.setServoPosition(2, 35);
  delay(500);
  cube_in();
  exc.resetEncoders(1);
  exc.resetEncoders(2);
  exc.setMotorTargets(L, -50, -20, -50, -20);
  exc.setMotorTargets(R, -50, -20, -50, -20);
  while (exc.readMotorBusy(1, 1)) {}
  grip_close_1();
  cube_out();
  funcflag = 0;
}

void macro_close_2()
{
  prizm.setServoPosition(3, 155);
  prizm.setServoPosition(4, 25);
  delay(500);
  cube_in();
  exc.resetEncoders(1);
  exc.resetEncoders(2);
  exc.setMotorTargets(L, -50, -20, -50, -20);
  exc.setMotorTargets(R, -50, -20, -50, -20);
  while (exc.readMotorBusy(1, 1)) {}
  grip_close_2();
  cube_out();
  funcflag = 0;
}

void macro_close_3()
{
  prizm.setServoPosition(5, 152);
  prizm.setServoPosition(6, 35);
  delay(500);
  cube_in();
  exc.resetEncoders(1);
  exc.resetEncoders(2);
  exc.setMotorTargets(L, -50, -20, -50, -20);
  exc.setMotorTargets(R, -50, -20, -50, -20);
  while (exc.readMotorBusy(1, 1)) {}
  grip_close_3();
  cube_out();
  funcflag = 0;
}

void macro_open_1()
{
  cube_in();
  exc.resetEncoders(1);
  exc.resetEncoders(2);
  exc.setMotorTargets(L, -50, -30, -50, -30);
  exc.setMotorTargets(R, -50, -30, -50, -30);
  while (exc.readMotorBusy(1, 1)) {}
  grip_open_1();
  cube_out();
  prizm.setServoPosition(1, 85);
  prizm.setServoPosition(2, 100);
  funcflag = 0;
}

void macro_open_2()
{
  cube_in();
  exc.resetEncoders(1);
  exc.resetEncoders(2);
  exc.setMotorTargets(L, -50, -30, -50, -30);
  exc.setMotorTargets(R, -50, -30, -50, -30);
  while (exc.readMotorBusy(1, 1)) {}
  grip_open_2();
  cube_out();
  prizm.setServoPosition(3, 90);
  prizm.setServoPosition(4, 90);
  funcflag = 0;
}

void macro_open_3()
{
  cube_in();
  exc.resetEncoders(1);
  exc.resetEncoders(2);
  exc.setMotorTargets(L, -50, -30, -50, -30);
  exc.setMotorTargets(R, -50, -30, -50, -30);
  while (exc.readMotorBusy(1, 1)) {}
  grip_open_3();
  cube_out();
  prizm.setServoPosition(5, 87);
  prizm.setServoPosition(6, 100);
  funcflag = 0;
}

void setup() {
  prizm.PrizmBegin();
  prizm.setServoSpeed(1, 50);
  prizm.setServoSpeed(2, 50);
  prizm.setServoSpeed(3, 50);
  prizm.setServoSpeed(4, 50);
  prizm.setServoSpeed(5, 50);
  prizm.setServoSpeed(6, 50);
  prizm.setServoPosition(1, 100);
  prizm.setServoPosition(2, 85);
  prizm.setServoPosition(3, 100);
  prizm.setServoPosition(4, 75);
  prizm.setServoPosition(5, 100);
  prizm.setServoPosition(6, 87);
  delay(1000);
  Serial.setTimeout(10);
  Serial.begin(9600);

  exc.setMotorInvert(1, 1, 1);
  exc.setMotorInvert(1, 2, 1);
  exc.setMotorInvert(2, 1, 0);
  exc.setMotorInvert(2, 2, 0);
  while (1)
  {
    Serial.println('z');
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
    while (funcflag == 1) {}
    Serial.println(command);
    command = 0;
  }
  if (command == 'l')
  {
    funcflag = 1;
    left();
    while (funcflag == 1) {}
    Serial.println(command);
    command = 0;
  }
  if (command == 'r')
  {
    funcflag = 1;
    right();
    while (funcflag == 1) {}
    Serial.println(command);
    command = 0;
  }
  if (command == 'j')
  {
    funcflag = 1;
    grip_left();
    while (funcflag == 1) {}
    Serial.println(command);
    command = 0;
  }
  if (command == 'k')
  {
    funcflag = 1;
    grip_right();
    while (funcflag == 1) {}
    Serial.println(command);
    command = 0;
  }
  if (command == 'e')
  {
    funcflag = 1;
    ending();
    while (funcflag == 1) {}
    Serial.println(command);
    command = 0;
  }
  if (command == '1')
  {
    funcflag = 1;
    macro_close_1();
    while (funcflag == 1) {}
    Serial.println(command);
    command = 0;
  }
  if (command == '3')
  {
    funcflag = 1;
    macro_close_2();
    while (funcflag == 1) {}
    Serial.println(command);
    command = 0;
  }
  if (command == '5')
  {
    funcflag = 1;
    macro_close_3();
    while (funcflag == 1) {}
    Serial.println(command);
    command = 0;
  }
  if (command == '2')
  {
    funcflag = 1;
    macro_open_1();
    while (funcflag == 1) {}
    Serial.println(command);
    command = 0;
  }
  if (command == '4')
  {
    funcflag = 1;
    macro_open_2();
    while (funcflag == 1) {}
    Serial.println(command);
    command = 0;
  }
  if (command == '6')
  {
    funcflag = 1;
    macro_open_3();
    while (funcflag == 1) {}
    Serial.println(command);
    command = 0;
  }
  if (command == 'f')
  {
    funcflag = 1;
    line();
    while (funcflag == 1) {}
    Serial.println(command);
    command = 0;
  }
  if (command == 's')
  {
    funcflag = 1;
    line_s();
    while (funcflag == 1) {}
    Serial.println(command);
    command = 0;
  }
}
