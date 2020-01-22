"""
[[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]
->
["Open", "Open", "Senior", "Open", "Open", "Senior"]
"""

def openOrSenior(data):
    #data is iterable
    lst=[]
    for d in data:
        if d[0]>=55 and d[1]>7:
            lst.append('Senior')
        else:
            lst.append('Open')
    return lst

data=[[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]
print(openOrSenior(data))
