#1) 패키지
#; 모듈들의 집합

# from calc.arith import *
#
# help(help(add))
# help(help(sub))
# help(help(mul))
# help(help(div))
#
# print(add.fadd(10, 20))
# print(sub.fsub(10, 20))
# print(mul.fmul(10, 20))
# print(div.fdiv(10, 20))

# from calc.shape import *
#
# help(circle)
# help(rectangle)
# help(triangle)
#
# print(circle.fcircle(3.4))
# print(rectangle.frectangle(3.5, 2.5))
# print(triangle.ftriangle(2.5, 2))

from calc.human import *

me = my.cmy("홍길동", 24, 100000000, "AR_VR", "3대 1000kg")
me.intro()
me.happy()
me.study()
me.health()