import serial
import time

# 시리얼 포트 설정
serial_port_1 = '/dev/ttyUSB0'  # 아두이노가 연결된 시리얼 포트 지정
serial_port_2 = '/dev/ttyUSB1'  # 아두이노가 연결된 시리얼 포트 지정
baud_rate = 9600  # 아두이노와 통신할 데이터 전송 속도 설정

# 시리얼 통신 연결
try: 
        arduino = serial.Serial(serial_port_1, baud_rate)
except:
        arduino = serial.Serial(serial_port_2, baud_rate)
time.sleep(2)  # 아두이노와의 연결이 안정화되기 위해 잠시 대기

#명령어 전송
def send_val(val):
        arduino.write(val.encode())
        arduino.flush()
        
#명령 수행 완료 확인
def wait_val(val):
        while True:
                response = arduino.readline()
                response_changed = response[:len(response)-1].decode(errors='ignore')
                if val in response_changed:
                        print(val)
                        break

def val_macro(val):
        send_val(val)
        wait_val(val)

def begin_serial():
        while True:
                print("Wait for Tetrix Prizm Connection...")
                response = arduino.readline()
                # 디코딩 후, 출력 (가장 끝의 \n을 없애주기위해 슬라이싱 사용)
                response_changed = response[:len(response)-1].decode(errors='ignore')
                print(response_changed)
                if "k" in response_changed:
                        print('connected')
                        arduino.write('p'.encode())
                        break
        arduino.flush()

begin_serial()
