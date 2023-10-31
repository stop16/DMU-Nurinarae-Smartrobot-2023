#include <PRIZM.h>

PRIZM prizm;
EXPANSION exc;
void setup() {
  // put your setup code here, to run once:
  prizm.PrizmBegin();
  prizm.setServoSpeed(1, 25);
  prizm.setServoSpeed(2, 25);
  prizm.setServoSpeed(3, 25);
  prizm.setServoSpeed(4, 25);
  prizm.setServoSpeed(5, 25);
  prizm.setServoSpeed(6, 25);
  exc.setMotorInvert(2, 1, 1);
  exc.setMotorInvert(2, 2, 1);
}

void close_1()
{
  prizm.setServoPosition(1,85);
  prizm.setServoPosition(2,100);
  delay(3000);
}

void close_2()
{
  prizm.setServoPosition(3,90);
  prizm.setServoPosition(4,90);
  delay(3000);
}

void close_3()
{
  prizm.setServoPosition(5,87);
  prizm.setServoPosition(6,100);
  delay(3000);
}

void open_1()
{
  prizm.setServoPosition(1,120);
  prizm.setServoPosition(2,65);
  delay(3000);
}

void open_2()
{
  prizm.setServoPosition(3,125);
  prizm.setServoPosition(4,55);
  delay(3000);
}

void open_3()
{
  prizm.setServoPosition(5,122);
  prizm.setServoPosition(6,65);
  delay(3000);
}

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

void loop() {
  // put your main code here, to run repeatedly:
  wheel(0,25,10);
  delay(1000);
  wheel(0,0,0);
  
  /*
  prizm.setServoPosition(6,91);
  delay(3000);
  prizm.setServoPosition(6,25);
  delay(3000);
  prizm.setServoPosition(6,158);
  delay(3000);
  */
  prizm.PrizmEnd();
}
