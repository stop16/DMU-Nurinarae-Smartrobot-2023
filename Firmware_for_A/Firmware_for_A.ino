#include<PRIZM.h>

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
  exc.setMotorTargets(1, 140, 235, 140, 235);
  exc.setMotorTargets(2, 140, 235, 140, 235);
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
      exc.setMotorSpeeds(1, 0, 0);
      exc.setMotorSpeeds(2, 0, 0);
      break;
    }
    else if (digitalRead(2) == 1 && digitalRead(3) == 0 && digitalRead(4) == 0)
    {
      exc.setMotorSpeeds(1, 65, 65);
      exc.setMotorSpeeds(2, 180, 180);
    }
    else if (digitalRead(2) == 0 && digitalRead(3) == 0 && digitalRead(4) == 1)
    {
      exc.setMotorSpeeds(1, 180, 180);
      exc.setMotorSpeeds(2, 65, 65);
    }
    else
    {
      exc.setMotorSpeeds(1, 180, 180);
      exc.setMotorSpeeds(2, 180, 180);
    }
  }
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

void ending()
{
  line_s(); // 마동지막 칸 까지 이
  //마지막 세개 인식 이후 동작임
  exc.resetEncoders(1);
  exc.resetEncoders(2);
  exc.setMotorTargets(1, 300, 720, -300, -720);
  exc.setMotorTargets(2, 300, 720, -300, -720);
  while (exc.readMotorBusy(1, 1)) {}
  exc.resetEncoders(1);
  exc.resetEncoders(2);
  exc.setMotorTargets(1, 300, 1240, 300, 1240);
  exc.setMotorTargets(2, 300, 1240, 300, 1240);
  while (exc.readMotorBusy(1, 1)) {}
  funcflag = 0;
}

void line_s()
{
  int lspd, rspd;
  lspd = rspd = 100;
  while (1) {
    exc.setMotorSpeeds(1, lspd, lspd);
    exc.setMotorSpeeds(2, rspd, rspd);
    if (digitalRead(2) == 1 && digitalRead(3) == 1 && digitalRead(4) == 1)
    {
      exc.setMotorSpeeds(1, 0, 0);
      exc.setMotorSpeeds(2, 0, 0);
      break;
    }
    if (digitalRead(2) == 1 && digitalRead(3) == 0 && digitalRead(4) == 0) //왼쪽
    {
      lspd = -100;
      rspd = 100;
    }
    if (digitalRead(2) == 0 && digitalRead(3) == 0 && digitalRead(4) == 1) //오른쪽
    {
      lspd = 100;
      rspd = -100;
    }
    if (digitalRead(2) == 0 && digitalRead(3) == 1 && digitalRead(4) == 0) //중앙
    {
      lspd = 100;
      rspd = 100;
    }
  }
}

void left()
{
  exc.setMotorSpeeds(1, -280, -280);
  exc.setMotorSpeeds(2, 280, 280);
  delay(400);
  while (1) {
    exc.setMotorSpeeds(1, -80, -80);
    exc.setMotorSpeeds(2, 80, 80);
    if (digitalRead(2) == 0 && digitalRead(3) == 1) {
      exc.setMotorSpeeds(1, 0, 0);
      exc.setMotorSpeeds(2, 0, 0);
      break;
    }
  }
  exc.setMotorSpeeds(1, -80, -80);
  exc.setMotorSpeeds(2, 80, 80);
  delay(90);
  exc.setMotorSpeeds(1, 0, 0);
  exc.setMotorSpeeds(2, 0, 0);
  funcflag = 0;
}

void left_s()
{

  while (1) {
    exc.setMotorSpeeds(1, -60, -60);
    exc.setMotorSpeeds(2, 60, 60);
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
  exc.setMotorSpeeds(1, 280, 280);
  exc.setMotorSpeeds(2, -280, -280);
  delay(400);
  while (1) {
    exc.setMotorSpeeds(1, 80, 80);
    exc.setMotorSpeeds(2, -80, -80);
    if (digitalRead(4) == 0 && digitalRead(3) == 1) {
      exc.setMotorSpeeds(1, 0, 0);
      exc.setMotorSpeeds(2, 0, 0);
      break;
    }
    
  }
  exc.setMotorSpeeds(1, 80, 80);
  exc.setMotorSpeeds(2, -80, -80);
  delay(90);
  exc.setMotorSpeeds(1, 0, 0);
  exc.setMotorSpeeds(2, 0, 0);
  funcflag = 0;
}

void right_s()
{
  while (1) {
    exc.setMotorSpeeds(1, 60, 60);
    exc.setMotorSpeeds(2, -60, -60);
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
        exc.setMotorSpeeds(1, -15, -15);
        exc.setMotorSpeeds(2, 15, 15);
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
        exc.setMotorSpeeds(1, 15, 15);
        exc.setMotorSpeeds(2, -15, -15);
        if (digitalRead(2) == 0 && digitalRead(3) == 1 && digitalRead(4) == 0)
        {
          break;
        }
      }
    }
    else
    {
      exc.setMotorSpeeds(1, 15, 15);
      exc.setMotorSpeeds(2, 15, 15);
    }
  }
  exc.setMotorSpeeds(1, 0, 0);
  exc.setMotorSpeeds(2, 0, 0);
}

void cube_out()
{
  exc.resetEncoders(1);
  exc.resetEncoders(2);
  exc.setMotorTargets(1, -120, -120, -120, -120);
  exc.setMotorTargets(2, -120, -120, -120, -120);
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
  exc.setMotorTargets(1, -50, -20, -50, -20);
  exc.setMotorTargets(2, -50, -20, -50, -20);
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
  exc.setMotorTargets(1, -50, -20, -50, -20);
  exc.setMotorTargets(2, -50, -20, -50, -20);
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
  exc.setMotorTargets(1, -50, -20, -50, -20);
  exc.setMotorTargets(2, -50, -20, -50, -20);
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
  exc.setMotorTargets(1, -50, -30, -50, -30);
  exc.setMotorTargets(2, -50, -30, -50, -30);
  while (exc.readMotorBusy(1, 1)) {}
  exc.resetEncoders(1);
  exc.resetEncoders(2);
  exc.setMotorTargets(1, 50, 10, -50, 10);
  exc.setMotorTargets(2, 50, 10, -50, 10);
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
  exc.setMotorTargets(1, -50, -30, -50, -30);
  exc.setMotorTargets(2, -50, -30, -50, -30);
  while (exc.readMotorBusy(1, 1)) {}
  exc.resetEncoders(1);
  exc.resetEncoders(2);
  exc.setMotorTargets(1, 50, 10, -50, 10);
  exc.setMotorTargets(2, 50, 10, -50, 10);
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
  exc.setMotorTargets(1, -50, -30, -50, -30);
  exc.setMotorTargets(2, -50, -30, -50, -30);
  while (exc.readMotorBusy(1, 1)) {}
  exc.resetEncoders(1);
  exc.resetEncoders(2);
  exc.setMotorTargets(1, 50, 10, -50, 10);
  exc.setMotorTargets(2, 50, 10, -50, 10);
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
  exc.setMotorInvert(2, 1, 1);
  exc.setMotorInvert(2, 2, 1);
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
}
