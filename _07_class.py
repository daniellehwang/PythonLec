# 1) class란?
# 함수 => 기능 function, 계산, 절차
# 기능들이 여러 개가 생겼다
# 기능들을 비슷한 종류로 묶고싶다
# 한번에 묶어서 관리하면 더 좋겠다
# = > 클래스
#
# 변수가 여러개
# 공통분모가 있다.
# 마치 사람의 이름, 나이, 주소 ...
# => 클래스
#
# 사람의 이름, 나이, 주소(변수)
#     행동, 정보 보여주기(함수)
# 공통분모(같은 종류)
# => 클래스

# a) 필드(변수) + 메서드(함수)들의 집합
# b) 시대가 흐르면서 함수보다 큰 단위가 프로그래밍 환경에 요구됨
# c) 명사(변수) + 동사(메서드)
#     문장의 최소 단위가 1형식 = 주어(명사)+동사 이듯이
#     프로그래밍에서도 변수+메서드의 결합을 통해서
#     프로그래밍의 독립단위를 묘사할 수 있다
# d) 클래스는 현실세계가 독립된 주체들의 상호작용으로 이루어지는 것처럼
#     클래스의 변수인 객체들간의 상호작용으로 프로그래밍을
#     처리할 수 있다
# e) 현실에서 privacy는 개인이 알아서 처리하고
#     상호 의존할 것은 소통을 통해서 처리하듯이
#     클래스도 내부에서 알아서 처리하는 부분과
#     외부와 상호작용하는 부분으로 나뉘어 진다

# 2) 클래스 제작
#     같은 속성들끼리 묶어서 관리한다
#     클래스는 객체를 만들어서 사용한다

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b

class Arith:
    def add(self, a, b):
        return a+b
    def sub(self, a, b):
        return a-b
    def mul(self, a, b):
        return a*b
    def div(self, a, b):
        return a/b

arith = Arith() #객체 생성
print(arith.add(10, 20))
print(arith.sub(10, 20))
print(arith.mul(10, 20))
print(arith.div(10, 20))