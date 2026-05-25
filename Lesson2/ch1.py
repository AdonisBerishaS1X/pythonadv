info1 = {
    "DANTE":"+3834355555"
}
info2 = {
    "MEPHISTON":"+3834355000"
}
info1["DANTE"]=4555
print(info1)

info2["MEPHISTON"]=2222
print(info2)

del info1["DANTE"]
print(info1)