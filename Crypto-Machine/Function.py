# 1. Wap to return a dictionary with characters and ascii value pair

def Values(a):
    Dic = {}
    for i in a:
        Dic[i] = ord(i)
        print(Dic)
Values('Shlok')