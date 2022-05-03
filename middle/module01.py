# 모듈 학습 방법1 - import
import math as m #as m 별명 변경

print(m.pi)
print(m.log10(30))
print(m.pow(2, 10))
print(2 ** 10)

# 모듈 학습 방법2 - from
from math import pow, log10, pi

print(pi)
print(log10(30))
print(pow(2, 10))
print(2 ** 10)