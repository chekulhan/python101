import sys
i = "Hola Mundo"
print(sys.getrefcount(i))
j = i
print(sys.getrefcount(i))
del j
print(sys.getrefcount(i))
# 4   , 5  , 4