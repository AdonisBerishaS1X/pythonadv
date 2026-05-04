users = {"DANTE","DANTE","MEPHISTON","LUCIEN"}

print("DANTE" in users)

print(users)

set1 = {1,2,3}
set2 = {3,4,5}


unionResults = set1.union(set2)

print("union of set1 and 2 usin union method",unionResults)

unionResults2 = set1 | set2

print("union of set1 and 2 usin | operator",unionResults2)


#
intersection_result1 = set1.intersection(set2)
print("intersection of set1 and 2 using inter method",intersection_result1)

intersection_result2 = set1 & set2
print("intersection of set1 and 2 using & method",intersection_result2)

difference_res1 = set1.difference(set2)
print("Difference betwen set 1 and 2 using difference method",difference_res1)

difference_res2 = set1- set2
print(difference_res2)

symetric = set1.symmetric_difference(set2)
print(symetric)

symetric2 = set1 ^ set2
print(symetric2)

myset = {1,2,3}

print(myset)

myset.add(7)
print(myset)