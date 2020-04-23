"""input: a list of six directions
north, west, east, south
the goal is to reduce unnececery steps
(north+south -> better to stay still)
"""

def dirReduc(arr):
    print('TESTING ARRAY:',arr)
    path=arr.copy()
    while True:
        indexes=[]
        solution=path.copy()
        print("STARTING SOLUTION:",solution)
        print("STARTING PATH:    ",path)
        for i in range(1,len(path)):
            print('DISPLAYING PAIRS: index["{}"]-"{}", index["{}"]-"{}"'.format(i-1,path[i-1],i,path[i]))
            if (path[i]=='NORTH' and path[i-1]=='SOUTH') or (path[i]=='SOUTH' and path[i-1]=='NORTH'):
                print('PAIR TO REMOVE FOUND:',i-1,path[i-1],i,path[i])
                print(path)
                print("removing",path[i],"index",i)
                path.pop(i)
                print(path)
                print("removing",path[i-1],"index",i-1)
                path.pop(i-1)
                print(path)
                break
            elif(path[i]=='WEST' and path[i-1]=='EAST') or (path[i]=='EAST' and path[i-1]=='WEST'):
                print('PAIR TO REMOVE FOUND:',i-1,path[i-1],i,path[i])
                print(path)
                print("removing",path[i],"index",i)
                path.pop(i)
                print(path)
                print("removing",path[i-1],"index",i-1)
                path.pop(i-1)
                print(path)
                break
        print("OPTIMIZED SOLUTION:",solution)
        print("OPTIMIZED PATH     ",path)
        if path==solution:
            print("The path cannot be more optimized")
            return path
        print("Trying futher optimization...")
        print(30*'-')

def test(path,result):
    if path==result:
        print("PATH: {}, SHOULD BE: {}, TEST PASSED".format(path,result))
    else:
        print("PATH: {}, SHOULD BE: {}, TEST FAILED".format(path,result))

'''
table={['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']:['WEST'],
      ['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'NORTH', 'SOUTH', 'NORTH', 'WEST', 'EAST']:['NORTH', 'NORTH'],
      []:[],
      ['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH']:[],
      ['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'NORTH']:['NORTH'],
      ['EAST', 'EAST', 'WEST', 'NORTH', 'WEST', 'EAST', 'EAST', 'SOUTH', 'NORTH', 'WEST']:['EAST', 'NORTH'],
      ['NORTH', 'EAST', 'NORTH', 'EAST', 'WEST', 'WEST', 'EAST', 'EAST', 'WEST', 'SOUTH']:['NORTH', 'EAST'],
      ['NORTH', 'WEST', 'SOUTH', 'EAST']:['NORTH', 'WEST', 'SOUTH', 'EAST'],
      ['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH', 'NORTH']:['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH'],
      ['NORTH', 'NORTH', 'WEST', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'WEST', 'SOUTH', 'SOUTH']:['NORTH', 'NORTH', 'WEST', 'NORTH', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH'],
      ['WEST', 'WEST', 'NORTH', 'NORTH', 'SOUTH', 'EAST', 'NORTH', 'WEST', 'NORTH', 'SOUTH']:['WEST', 'WEST', 'NORTH', 'EAST', 'NORTH', 'WEST'],
      ['EAST', 'NORTH', 'SOUTH', 'EAST', 'SOUTH', 'NORTH', 'EAST', 'NORTH', 'EAST', 'WEST']:['EAST', 'EAST', 'EAST', 'NORTH']
       }

for (a,b) in table:
    test(a,b)
'''
test(dirReduc(['EAST', 'EAST', 'WEST', 'NORTH', 'WEST', 'EAST', 'EAST', 'SOUTH', 'NORTH', 'WEST']),['EAST', 'NORTH'])

