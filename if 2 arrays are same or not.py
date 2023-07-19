a=[3,5,7,8]
b=[7,3,8,4]
print(len(a))
print(len(b))
if len(a)==len(b):
    for i in len(a):
        for j in len(b):
            if a[i]==b[j]:
                print("arrays are same")
            else:
                print("arrays are not same")
else:
    print("arrays are not same")
