#2023 Smartrobot Algorithm

#import libraries
from color_detection_test import *
#from serialtest import *

#create 2 Virtual Map(Pillar & Cube) and initialize to 0
VM_Pillar = [
    [0,0],
    [0,0],
    [0,0],
    [0,0]
]
VM_Cube = [
    [0,0],
    [0,0],
    [0,0],
    [0,0]
]

#Define list of colors
color = ['Red', 'Green', 'Blue', 'Yellow', 'None']

#Define list of directions
robot_dir = ['Front', 'Rear', 'Left', 'Right']

#Virtual map value changing function
"""
y : 큐브 또는 기둥의 y위치, 0번부터 3번까지 존재함. 숫자가 커질수록 시작지점에 가까워짐.
x : 큐브 또는 기둥의 x위치, 0번부터 1번까지 존재함. 0번은 Finish측, 1번은 Start측임.
val : 큐브 또는 기둥의 색깔, Red, Green, Blue, Yellow, None이 있음. None은 큐브가 없음을 의미함.
"""
def change_pillar(y,x,val):
    VM_Pillar[y][x] = val
    if x == 0:
        VM_Pillar[y][1] = color[4]
    elif x == 1:
        VM_Pillar[y][0] = color[4]

def change_cube(y,x,val):
    VM_Cube[y][x] = val
    if x == 0:
        VM_Cube[y][1] = color[4]
    elif x == 1:
        VM_Cube[y][0] = color[4]

def pack_cube():
    for i in range(0,4):
        if VM_Cube[i][0] == 0 and VM_Cube[i][1] == 0:
            VM_Cube[i][0] = color[4]
            VM_Cube[i][1] = color[4]

#Rule checking function
"""
errflag : Rule Check 후 에러 유무 표시
0 : 에러 없음
1 : 오류 발생

발생할 수 있는 오류의 경우
1. 노랑 기둥이 아닌, 다른 기둥 위에 큐브가 없는 경우
2. 노랑 기둥 위에 큐브가 있는 경우
3. 기둥과 큐브의 색이 일치하는 경우
4. 기둥이 없고 큐브만 있는 경우
5. 같은 색의 큐브가 여러개 있는 경우
6. 같은 색의 기둥이 여러개 있는 경우
"""
def rule_check(vm_pillar, vm_cube):
    errflag = [0,0,0,0,0,0]
    cnt_c_r = cnt_c_g = cnt_c_b = 0
    cnt_p_r = cnt_p_g = cnt_p_b = cnt_p_y = 0
    for i in range(0,4):
        if (vm_cube[i] == [color[4], color[4]]) and (vm_pillar[i][0] != color[3] and vm_pillar[i][1] != color[3]):
            print("오류 : 기둥 위에 큐브가 없습니다. 위치(y) : "+str(i))
            errflag[0] = 1
        if (vm_pillar[i][0] == color[3] and vm_cube[i][0] != color[4]) or (vm_pillar[i][1] == color[3] and vm_cube[i][1] != color[4]):
            print("오류 : 노랑 기둥 위에 큐브가 있습니다. 위치(y) : "+str(i))
            errflag[1] = 1
        if ((vm_pillar[i][0] == vm_cube[i][0]) and vm_cube[i][0] != color[4]) or ((vm_pillar[i][1] == vm_cube[i][1]) and vm_cube[i][1] != color[4]):
            print("오류 : 기둥과 큐브 색이 일치합니다. 위치(y) : "+str(i))
            errflag[2] = 1
        if (vm_cube[i][0] != color[4] and vm_pillar[i][0] == color[4]) or (vm_cube[i][1] != color[4] and vm_pillar[i][1] == color[4]):
            print("오류 : 기둥이 없고 큐브만 있습니다. 위치(y) : "+str(i))
            errflag[3] = 1
        for j in range(0,2):
            if vm_cube[i][j] == color[0]:
                cnt_c_r += 1
            if vm_cube[i][j] == color[1]:
                cnt_c_g += 1
            if vm_cube[i][j] == color[2]:
                cnt_c_b += 1
            if vm_pillar[i][j] == color[0]:
                cnt_p_r += 1
            if vm_pillar[i][j] == color[1]:
                cnt_p_g += 1
            if vm_pillar[i][j] == color[2]:
                cnt_p_b += 1
            if vm_pillar[i][j] == color[3]:
                cnt_p_y += 1
    if (cnt_c_r != 1 or cnt_c_g != 1 or cnt_c_b != 1):
        print("오류 : 같은 색의 큐브가 여러개 있습니다.")
        errflag[4] = 1
    if (cnt_p_r != 1 or cnt_p_g != 1 or cnt_p_b != 1 or cnt_p_y != 1):
        print("오류 : 같은 색의 기둥이 여러개 있습니다.")
        errflag[5] = 1
            
    return errflag

#Utility functions
#1. Search Color
def search_color(vm,color,startfrom=0):
    breakflag = 0
    for i in range(startfrom,4):
        for j in range(0,2):
            if vm[i][j] == color:
                breakflag = 1
                break
        if breakflag == 1:
            break
    return [i,j]
#2. Get numbers of color
def get_num(vm, color):
    num = 0
    for i in range(0,4):
        for j in range(0,2):
            if vm[i][j] == color:
                num +=1
    return num
#3. Get direction of cube
def get_dir(vm,y):
    if vm[y][0] != color[4]:
        return 0
    elif vm[y][1] != color[4]:
        return 1
    else:
        return 2

#Auto correction function
"""
errflag 기반 자동 문제 해결시 경우의 수
1. 같은 색 큐브가 여러개 있고, 노랑 기둥 위에 큐브가 있을 경우 -> 노랑 기둥 위의 큐브를 제거
2. 같은 색 큐브가 여러개 있고, 기둥과 큐브의 색이 일치하는 경우 -> 겹친 색상의 큐브를 남는 색상으로 변경
3. 같은 색 기둥이 여러개 있고, 노랑 기둥이 없을 경우 -> 위에 큐브가 없는 기둥을 노랑으로 변경
4. 노랑 기둥이 여러개일 경우 -> 위에 큐브가 없는 기둥을 노랑으로 유지, 남은 기둥을 남는 색상으로 변경
5. TBD
"""
def auto_correction(vm_pillar, vm_cube, errflag):
    print("Auto-Correction is working...")
    if errflag[4] == 1 and errflag[1] == 1:
        tmpxy = search_color(vm_pillar,color[3])
        vm_cube[tmpxy[0]][tmpxy[1]] = color[4]
    
    if errflag[4] == 1 and errflag[2] == 1:
        for i in range(0,3):
            if get_num(vm_cube, color[i]) != 1:
                break
        for j in range(0,3):
            tmpnum = get_num(vm_cube,color[j])
            if tmpnum == 0:
                break
        tmpxy = search_color(vm_cube,color[i])
        if tmpxy == search_color(vm_pillar,color[i]):
            vm_cube[tmpxy[0]][tmpxy[1]] = color[i]
        else:
            tmpxy = search_color(vm_cube,color[i],tmpxy[0] + 1)
            vm_cube[tmpxy[0]][tmpxy[1]] = color[j]

    if errflag[5] == 1 and get_num(vm_pillar, color[3]) == 0:
        breakflag = 0
        for i in range(0,4):
            for j in range(0,2):
                if vm_pillar[i][j] != color[4] and vm_cube[i][j] == color[4]:
                    breakflag = 1
                    break
            if breakflag == 1:
                break
        vm_pillar[i][j] = color[3]
    if errflag[5] == 1 and get_num(vm_pillar,color[3]) > 1:
        tmpxy = search_color(vm_pillar,color[3])
        for i in range(0,4):
            if get_num(vm_pillar, color[i]) == 0:
                break
        if vm_cube[tmpxy[0]][tmpxy[1]] != color[4]:
            vm_pillar[tmpxy[0]][tmpxy[1]] = color[i]
        else:
            tmpxy = search_color(vm_pillar,color[3],tmpxy[0] + 1)
            vm_pillar[tmpxy[0]][tmpxy[1]] = color[i]

#Cube storing function
cube_storage = ['None', 'None', 'None']
def store_cube(name):
    global cube_storage
    if cube_storage[0] == 'None':
        cube_storage[0] = name
    elif cube_storage[1] == 'None':
        cube_storage[1] = name
    elif cube_storage[2] == 'None':
        cube_storage[2] = name
def get_available_storage():
    global cube_storage
    if cube_storage[0] == 'None':
        return 0
    elif cube_storage[1] == 'None':
        return 1
    elif cube_storage[2] == 'None':
        return 2
def find_in_storage(name):
    global cube_storage
    for i in range(0,3):
        if cube_storage[i] == name:
            break
    return i
def print_storage():
    global cube_storage
    print("Storage :", cube_storage)
def eject_cube(name):
    global cube_storage
    cube_storage[find_in_storage(name)] = 'None'
#Path create function
"""
미션 수행 알고리즘
YellowFlag 설정 : [flag, y] 형식으로 Yellow Cube가 있는 위치 저장
0. #4에서 #3으로 이동
1. #3에서 색인식 후 노랑기둥이 아니라면 1-1 수행, 노랑기둥이라면 1-2 수행.
    1-1. 큐브방향으로 돌아서 잡고 나와서 그립 회전 후 #2로 이동.
    1-2. YellowFlag 활성화 후 #2로 이동.
2. #2에서 색인식 후 노랑기둥이 아니라면 2-1 수행, 노랑기둥이라면 2-2수행.
    2-1. 큐브방향으로 돌아서 잡고 나와서 그립 회전 후 #1로 이동.
    2-2. YellowFlag 활성화 후 #1로 이동.
3. #1에서 색인식 후 노랑기둥이 아니라면 3-1 수행, 노랑기둥이라면 3-2 수행.
    3-1. 큐브방향으로 돌아서 잡고 나와서 그립 회전 후 #0으로 이동.
    3-2. YellowFlag 활성화 후 #0으로 이동.
4. YellowFlag가 활성화 되어있다면 4-1 수행, 활성화 되어있지 않다면 4-2 수행.
    4-1.
        1. 색인식 후 큐브방향으로 돌아서 잡고 나옴.
        2. 기둥 색깔에 맞는 큐브색깔로 변경 후 다시 놓고 나옴.
        3. #1로 이동.
    4-2. #1로 이동.
5. YellowFlag의 y값이 1이면 5-1 수행, 아니라면 5-2 수행.
    5-1. #2로 이동.
    5-2. 큐브방향으로 돌아서 기둥 색깔에 맞는 큐브색깔로 변경 후 놓고 나옴, #2로 이동.
6. YellowFlag의 y값이 2면 6-1 수행, 아니라면 6-2 수행.
    6-1. #3으로 이동.
    6-2. 큐브방향으로 돌아서 기둥 색깔에 맞는 큐브색깔로 변경 후 놓고 나옴, #3으로 이동.
7. YellowFlag의 y값이 3이면 7-1 수행, 아니라면 7-2 수행.
    7-1. #4로 이동.
    7-2. 큐브방향으로 돌아서 기둥 색깔에 맞는 큐브색깔로 변경 후 놓고 나옴, #4로 이동.
8. Finish
"""
"""
Log 설명
1. Move : #y -> y좌표로 이동, 로봇 이동시에는 Forward임.
2. Turn : Left or Right -> 좌회전 또는 우회전을 함
3. Grip : Storagenum -> 잡아오기
4. SpinGrip : Storagenum -> 그립 회전으로 원하는 색상으로 변경
5. Check : [Pillar_Color,Cube_Color] -> 색인식, 위쪽 큐브와 아래쪽 기둥으로 VM에 저장함
6. CurrentDir : Dirname -> 현재 로봇의 방향을 표시함
7. YellowFlag enabled at : YellowFlag가 설정된 지점 표시함
"""
current_dir = 0
def path_creation(vm_pillar, vm_cube, current_loc=4):
    YellowFlag = [0,-1]
    print("Path Creation Started!")
    global current_dir
    #0
    print("Current location(y) : "+str(current_loc))
    if current_loc == 4:
        print("CurrentDir : " + robot_dir[0])
        current_dir = robot_dir[0]
        print("Move : #3")
        current_loc = 3

        #1
        #1-1
        print("Check : " + str(vm_pillar[current_loc]) + str(vm_cube[current_loc]))
        if get_dir(vm_cube, current_loc) == 0:
            print("Turn : Left")
            print("CurrentDir : " + robot_dir[2])
            current_dir = robot_dir[2]

            print("Grip : Storagenum " + str(get_available_storage()))
            store_cube(vm_cube[current_loc][0])
            print_storage()

            print("Turn : Right")
            print("CurrentDir : " + robot_dir[0])
            current_dir = robot_dir[0]
            print("Move : #2")
            current_loc = 2
        elif get_dir(vm_cube, current_loc) == 1:
            print("Turn : Right")
            print("CurrentDir : " + robot_dir[3])
            current_dir = robot_dir[3]

            print("Grip : Storagenum " + str(get_available_storage()))
            store_cube(vm_cube[current_loc][1])
            print_storage()

            print("Turn : Left")
            print("CurrentDir : " + robot_dir[0])
            current_dir = robot_dir[0]
            print("Move : #2")
            current_loc = 2

        #1-2
        elif get_dir(vm_cube, current_loc) == 2:
            YellowFlag[0] = 1
            YellowFlag[1] = current_loc
            print("YellowFlag enabled at : "+str(YellowFlag[1]))
            print("Move : #2")
            current_loc = 2

        #2
        #2-1
        print("Check : " + str(vm_pillar[current_loc]) + str(vm_cube[current_loc]))
        if get_dir(vm_cube, current_loc) == 0:
            print("Turn : Left")
            print("CurrentDir : " + robot_dir[2])
            current_dir = robot_dir[2]

            print("Grip : Storagenum " + str(get_available_storage()))
            store_cube(vm_cube[current_loc][0])
            print_storage()

            print("Turn : Right")
            print("CurrentDir : " + robot_dir[0])
            current_dir = robot_dir[0]
            print("Move : #1")
            current_loc = 1
        elif get_dir(vm_cube, current_loc) == 1:
            print("Turn : Right")
            print("CurrentDir : " + robot_dir[3])
            current_dir = robot_dir[3]
            
            print("Grip : Storagenum " + str(get_available_storage()))
            store_cube(vm_cube[current_loc][1])
            print_storage()

            print("Turn : Left")
            print("CurrentDir : " + robot_dir[0])
            current_dir = robot_dir[0]
            print("Move : #1")
            current_loc = 1

        #2-2
        elif get_dir(vm_cube, current_loc) == 2:
            YellowFlag[0] = 1
            YellowFlag[1] = current_loc
            print("YellowFlag enabled at : "+str(YellowFlag[1]))
            print("Move : #1")
            current_loc = 1
        
        #3
        #3-1
        print("Check : " + str(vm_pillar[current_loc]) + str(vm_cube[current_loc]))
        if get_dir(vm_cube, current_loc) == 0:
            print("Turn : Left")
            print("CurrentDir : " + robot_dir[2])
            current_dir = robot_dir[2]

            print("Grip : Storagenum " + str(get_available_storage()))
            store_cube(vm_cube[current_loc][0])
            print_storage()

            print("Turn : Right")
            print("CurrentDir : " + robot_dir[0])
            current_dir = robot_dir[0]
            print("Move : #0")
            current_loc = 0
        elif get_dir(vm_cube, current_loc) == 1:
            print("Turn : Right")
            print("CurrentDir : " + robot_dir[3])
            current_dir = robot_dir[3]
            
            print("Grip : Storagenum " + str(get_available_storage()))
            store_cube(vm_cube[current_loc][1])
            print_storage()

            print("Turn : Left")
            print("CurrentDir : " + robot_dir[0])
            current_dir = robot_dir[0]
            print("Move : #0")
            current_loc = 0

        #3-2
        elif get_dir(vm_cube, current_loc) == 2:
            YellowFlag[0] = 1
            YellowFlag[1] = current_loc
            print("YellowFlag enabled at : "+str(YellowFlag[1]))
            print("Move : #0")
            current_loc = 0
        
        #4
        #4-1
        if YellowFlag[0] == 1:
            print("Check : " + str(vm_pillar[current_loc]) + str(vm_cube[current_loc]))
            if get_dir(vm_cube, current_loc) == 0:
                print("Turn : Left")
                print("CurrentDir : " + robot_dir[2])
                current_dir = robot_dir[2]

                print("Grip : Storagenum " + str(get_available_storage()))
                store_cube(vm_cube[current_loc][0])
                print_storage()

                print("SpinGrip : " + cube_storage[find_in_storage(vm_pillar[current_loc][0])])
                vm_cube[current_loc][0] = cube_storage[find_in_storage(vm_pillar[current_loc][0])]
                eject_cube(cube_storage[find_in_storage(vm_pillar[current_loc][0])])
                print_storage()

                print("Turn : Left")
                print("CurrentDir : " + robot_dir[1])
                current_dir = robot_dir[1]
                print("Move : #1")
                current_loc = 1
            elif get_dir(vm_cube, current_loc) == 1:
                print("Turn : Right")
                print("CurrentDir : " + robot_dir[3])
                current_dir = robot_dir[3]
                
                print("Grip : Storagenum " + str(get_available_storage()))
                store_cube(vm_cube[current_loc][1])
                print_storage()

                print("SpinGrip : " + cube_storage[find_in_storage(vm_pillar[current_loc][1])])
                vm_cube[current_loc][1] = cube_storage[find_in_storage(vm_pillar[current_loc][1])]
                eject_cube(cube_storage[find_in_storage(vm_pillar[current_loc][1])])
                print_storage()

                print("Turn : Right")
                print("CurrentDir : " + robot_dir[1])
                current_dir = robot_dir[1]
                print("Move : #1")
                current_loc = 1
        #4-2
        else:
            print("Turn : Right")
            print("Turn : Right")
            current_dir = robot_dir[1]
            print("CurrentDir : " + current_dir)
            print("Move : #1")
            current_loc = 1
        
        #5
        #5-1
        if YellowFlag[1] == current_loc:
            print("Move : #2")
            current_loc = 2

        #5-2
        else:
            if get_dir(vm_cube, current_loc) == 0:
                print("Turn : Right")
                current_dir = robot_dir[2]
                print("CurrentDir : " + current_dir)
                print("SpinGrip : " + cube_storage[find_in_storage(vm_pillar[current_loc][0])])
                vm_cube[current_loc][0] = cube_storage[find_in_storage(vm_pillar[current_loc][0])]
                eject_cube(cube_storage[find_in_storage(vm_pillar[current_loc][0])])
                print_storage()
                print("Turn : Left")
                current_dir = robot_dir[1]
                print("CurrentDir : " + current_dir)
                print("Move : #2")
                current_loc = 2

            elif get_dir(vm_cube, current_loc) == 1:
                print("Turn : Left")
                current_dir = robot_dir[3]
                print("CurrentDir : " + current_dir)
                print("SpinGrip : " + cube_storage[find_in_storage(vm_pillar[current_loc][1])])
                vm_cube[current_loc][1] = cube_storage[find_in_storage(vm_pillar[current_loc][1])]
                eject_cube(cube_storage[find_in_storage(vm_pillar[current_loc][1])])
                print_storage()
                print("Turn : Right")
                current_dir = robot_dir[1]
                print("CurrentDir : " + current_dir)
                print("Move : #2")
                current_loc = 2
        
        #6
        #6-1
        if YellowFlag[1] == current_loc:
            print("Move : #3")
            current_loc = 3
        
        #6-2
        else:
            if get_dir(vm_cube, current_loc) == 0:
                print("Turn : Right")
                current_dir = robot_dir[2]
                print("CurrentDir : " + current_dir)
                print("SpinGrip : " + cube_storage[find_in_storage(vm_pillar[current_loc][0])])
                vm_cube[current_loc][0] = cube_storage[find_in_storage(vm_pillar[current_loc][0])]
                eject_cube(cube_storage[find_in_storage(vm_pillar[current_loc][0])])
                print_storage()
                print("Turn : Left")
                current_dir = robot_dir[1]
                print("CurrentDir : " + current_dir)
                print("Move : #3")
                current_loc = 3

            elif get_dir(vm_cube, current_loc) == 1:
                print("Turn : Left")
                current_dir = robot_dir[3]
                print("CurrentDir : " + current_dir)
                print("SpinGrip : " + cube_storage[find_in_storage(vm_pillar[current_loc][1])])
                vm_cube[current_loc][1] = cube_storage[find_in_storage(vm_pillar[current_loc][1])]
                eject_cube(cube_storage[find_in_storage(vm_pillar[current_loc][1])])
                print_storage()
                print("Turn : Right")
                current_dir = robot_dir[1]
                print("CurrentDir : " + current_dir)
                print("Move : #3")
                current_loc = 3
        
        #7
        #7-1
        if YellowFlag[1] == current_loc:
            print("Move : #4")
            current_loc = 4
        
        #7-2
        else:
            if get_dir(vm_cube, current_loc) == 0:
                print("Turn : Right")
                current_dir = robot_dir[2]
                print("CurrentDir : " + current_dir)
                print("SpinGrip : " + cube_storage[find_in_storage(vm_pillar[current_loc][0])])
                vm_cube[current_loc][0] = cube_storage[find_in_storage(vm_pillar[current_loc][0])]
                eject_cube(cube_storage[find_in_storage(vm_pillar[current_loc][0])])
                print_storage()
                print("Turn : Left")
                current_dir = robot_dir[1]
                print("CurrentDir : " + current_dir)
                print("Move : #4")
                current_loc = 4

            elif get_dir(vm_cube, current_loc) == 1:
                print("Turn : Left")
                current_dir = robot_dir[3]
                print("CurrentDir : " + current_dir)
                print("SpinGrip : " + cube_storage[find_in_storage(vm_pillar[current_loc][1])])
                vm_cube[current_loc][1] = cube_storage[find_in_storage(vm_pillar[current_loc][1])]
                eject_cube(cube_storage[find_in_storage(vm_pillar[current_loc][1])])
                print_storage()
                print("Turn : Right")
                current_dir = robot_dir[1]
                print("CurrentDir : " + current_dir)
                print("Move : #4")
                current_loc = 4
        
        #8
        print("Finish!")
        print(vm_pillar)
        print(vm_cube)

"""
#Test area
change_cube(3,0,color[1])
change_cube(2,0,color[0])
change_cube(1,1,color[2])

change_pillar(3,0,color[2])
change_pillar(2,0,color[1])
change_pillar(1,1,color[0])
change_pillar(0,0,color[3])

pack_cube()
print(VM_Cube)
print(VM_Pillar)
err = rule_check(VM_Pillar,VM_Cube)
print(err)
if err != [0,0,0,0,0,0]:
    auto_correction(VM_Pillar,VM_Cube,err)
print(VM_Cube)
print(VM_Pillar)
"""
path_creation(VM_Pillar,VM_Cube)
