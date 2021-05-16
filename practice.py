# if문

# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and 30 > temp:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요.")

# 반복 for

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waitng_no in range(1, 6): # 1 ~ 6 직전까지
#     print("대기번호 : {0}".format(waitng_no))

# starbucks = ["아이언맨", "토르", "그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

# 반복 while

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer,index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분 되었습니다.")

# customer = "아이언맨" #무한 루프
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unknown"

# while person != customer : 
#         print("{0}, 커피가 준비되었습니다.".format(customer))
#         person = input("이름이 어떻게 되세요? ")

# continue는 만나면 건너 뛰고 다음 반복으로 계속 진행
# break 만나면 바로 반복문 탈출

# absent = [2, 5] # 결석
# no_book = [7] # 책 깜빡
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("이런 ㅅㅂ 놈이... {0} 너 나와!".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

# 한줄 for문 출석번호 1,2,3,4 앞에 100을 붙이기로 함
# student = [1,2,3,4,5]
# print(student)
# student = [i+100 for i in student]
# print(student)

# 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# 학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

from random import *
count = 0
for i in range(1,51):
    time = int(random()*46 + 5)
    #time = randrange(5,51) 이런 쉬운 방법이...
    if time > 15:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
    else:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        count=count+1
        #count += 1
print("\n총 탑승 승객 : {0} 분".format(count))
