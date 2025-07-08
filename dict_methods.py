#---Update()---

ep1 = {122 : 45 , 123 : 87 , 345 : 69 , 234 : 69}
ep2 = {334 : 21 , 455 : 33}
ep1.update(ep2)
print(ep1)

#----clear---

ep1 = {122 : 45 , 123 : 87 , 345 : 69 , 234 : 69}
ep2 = {334 : 21 , 455 : 33}
ep1.clear()
print(ep1)
# Empty dictionary
empty = {}
print(empty)

# ----POP()----

ep1 = {122 : 45 , 123 : 87 , 345 : 69 , 234 : 69}
ep2 = {334 : 21 , 455 : 33}
ep1.pop(122)
print(ep1)
ep1.popitem()  # pop up the last value
print(ep1)

#---del()---

ep1 = {122 : 45 , 123 : 87 , 345 : 69 , 234 : 69}
ep2 = {334 : 21 , 455 : 33}
del ep1
del ep1[122]
print(ep1)
