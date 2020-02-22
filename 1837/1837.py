A, B, C = input("").split()
A = int(A)
B = int(B)
C = int(C)

# A = 4
# B = 6
# C = 7

if (A > B and C >= B ):
    print(":)")
elif(B > A and B >= C):
    print(":(")
elif(A < B and B < C ):
    if abs(A-B) > abs(B-C):
        print(":(")
    else:
        print(":)")
elif (A > B and B > C):
    if abs(A-B) > abs(B-C):
        print(":)")
    else:
        print(":(")
elif (A == B ):
    if C > B:
        print(":)")
    else:
        print(":(")
