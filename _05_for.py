# for문은 while문과 상호치환할 수 있다
# 다만 명시적인 시작과 끝이 있을 때 사용
# while문 보다 사용빈도가 높다

# 1) 나무를 10번 찍기
# for i in range(1,11): # 1 ~ 10까지
#     print("나무를 {0}번 찍는다".format(i))

# 2) 리스트, 튜플과 함께 사용하기
# datas = [2,4,6,8,10]
# for num in datas:
#     print(num, end=", ")
# print()
#
# datas = (10,20,30,40,50)
# for num in datas:
#     print(num, end=", ")
# print()

# 3) range 함수와 사용
# for i in range(10,21):
#     print(i, end = " ")
# print()
#
# # 2씩 증가
# for i in range(10, 101, 2):
#     print(i, end=" ")
# print()
#
# for i in range(100, 0, -2):
#     print(i, end=" ")
# print()



# 4) 1~100까지 누적합을 구하세요
#A, B,C를 다른 숫자나 변수로 채우시오
# total = 0
# for i in range(1,101):
#     total += i
# 
# print("1~100의 누적합은", total)


# 5) 정수를 입력받아 누적하고, "end"를 입력하면 누적값을 출력하세요
# total = 0
# while True:
#     sInput = input("정수를 입력하세요 >> ")
#     if sInput == "end":
#         break
#     elif sInput.isdigit(): #숫자로 변환 가능하냐?
#         total += int(sInput)
#     else:
#         print("정수가 아닙니다8")
#
# print("누적합은 ", total)

# 6) 정수를 입력받아 저장하고, "end"를 입력하면 입력한 순서대로 모든 정수 출력
# nums = []
# while True:
#     sInput = input("정수를 입력하세요 >> ")
#     if sInput == "end":
#         break
#     elif sInput.isdigit():  # 숫자로 변환 가능하냐?
#         nums.append(int(sInput))
#     else:
#         print("정수가 아닙니다8")
#
# print("입력한 값은 ", nums)

# 7) 구구단 3단을 출력하세요
# for i in range(1, 10):
#     print("{0} x {1} = {2}".format(3, i, 3*i))
#
# 7) 구구단 9단을 역순으로 출력하세요
# for i in range(9, 0, -1):
#     print("{0} x {1} = {2}".format(9, i, 9*i))

# 8) 구구단 9단을 짝수만 출력
# 9x2. 9x4, 9x6
#

# 2중  for 문 사용
# 9) 구구단 전체를 출력하세요
# 2~9단까지
#
# 10) 구구단 전체를 출력하는데 각 단을 세로로 출력하세요

# 11) 리스트 내포
# datas = []
# for i in range(0,10):
#     datas.append(i)
#
# print(datas)

# datas = [i for i in range(0, 10)]
# print(datas)
#
# datas = [i*2 for i in range(0, 10)]
# print(datas)
#
# datas = [i*3 for i in range(0, 10)]
# print(datas)
#
#
#
# datas = [i*3 for i in range(0, 10) if i%2 == 0]
# print(datas)
# #위와 동일
# datas = []
# for i in range(0,10):
#     if i%2 == 0:
#         datas.append(i*3)
#
# print(datas)
#
#
#print(datas)