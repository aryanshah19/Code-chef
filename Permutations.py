def Permutations(a, length=0):
        if length == len(a):
            print(a)
        else:
            for i in range(length, len(a)):
                a[length], a[i] = a[i] ,a[length]
                Permutations(a, length+1)
                a[length], a[i] = a[i], a[length]
list=list(map(int,input("Input all the elements of the list:\n").split()))
print(Permutations(list)) 