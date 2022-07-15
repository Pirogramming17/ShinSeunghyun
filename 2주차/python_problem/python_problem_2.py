#함수 이름은 변경 가능합니다.

##############  menu 1
student_list = []

class Student:
    def __init__(self, name, mid, fin, grade):
        self.name = name
        self.mid = mid
        self.fin = fin
        self.grade = grade

    def grade_cal(self):
        grade = (self.mid + self.fin) // 2
        #같은 클래스 내 요소 self 빼먹지 말기!
        if grade >= 90:
            self.grade = 'A'
        elif grade >= 80:
            self.grade = 'B'
        elif grade >= 70:
            self.grade = 'C'
        else:
            self.grade = 'D'

class Menu:
    def __init__(self):
        pass

    def Menu1(name, mid, final) :
        #사전에 학생 정보 저장하는 코딩
        student_list.append(Student(name, mid, final, 0))

    ##############  menu 2
    def Menu2():
        #학점 부여 하는 코딩
        for i in range(len(student_list)):
            if student_list[i].grade == 0:
                student_list[i].grade_cal()

    ##############  menu 3
    def Menu3() :
        print('----------------------')
        print('name mid final grade')
        print('----------------------')
        for i in range(len(student_list)):
            print(student_list[i].name, student_list[i].mid, student_list[i].fin, student_list[i].grade)

    ##############  menu 4
    def Menu4(name):
        for i in range(len(student_list)):
            if name == student_list[i].name:
                del student_list[i]


    #학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        #학생 정보 입력받기
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        #예외사항이 아닌 입력인 경우 1번 함수 호출
        try:
            name, mid, fin = input('Enter name mid-score final-score :').split()
        except ValueError:
            print("Please enter 3 data")
        else:
            #처음엔 비어있기 때문에 for문과 리스트로 '먼저 접근하는' 예외처리 불가
            overlap_name = 0
            for i in range(len(student_list)):
                if name == student_list[i].name:
                    overlap_name += 1
            if overlap_name > 0:
                print('That name already exists')
            else:
                try:
                    mid = int(mid)
                    fin = int(fin)
                except ValueError:
                    print('Please enter positive integer!')
                else:
                    if mid < 0 or fin < 0:
                        print('Please enter positive integer!')
                    else:
                        Menu.Menu1(name, mid, fin)

    elif choice == "2" :
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우 2번 함수 호출
        #"Grading to all students." 출력
        if len(student_list) == 0:
            print('No student data!')
        else:
            Menu.Menu2()
            print('Grading to all students.')
            print(student_list[0].grade)

    elif choice == "3" :
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        #예외사항이 아닌 경우 3번 함수 호출
        if len(student_list) == 0:
            print('No student data!')
        else:
            for i in range(len(student_list)):
                if student_list[i].grade == 0:
                    print("Some students didn't get grade")
                    break
                if len(student_list) - 1 == i:
                    # Menu3 실행부에 조건을 걸지 않으면 등급을 못받은 학생이 있어도
                    # Menu3가 실행됨.
                    Menu.Menu3()


    elif choice == "4" :
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력
        if len(student_list) == 0:
            print('No student data!')
        else:
            del_student = input('Enter the name to delete : ')
            for i in range(len(student_list)):
                if del_student == student_list[i].name:
                    Menu.Menu4(del_student)
                    print(f'{del_student} student information is deleted.')
                    break
                if i == len(student_list)-1:
                    print("Not exist name!")



    elif choice == "5" :
        #프로그램 종료 메세지 출력
        #반복문 종료
        print("Exit Program!")
        break

    else :
        print('wrong number. choose again')
        #"Wrong number. Choose again." 출력