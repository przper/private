def bouncingBall(h, bounce, window):
    print(h,bounce,window)
    if h<=0 or bounce<0 or bounce>=1 or window>=h:
        return -1
    else:
        num=0 #number of bounces
        while True:
            print("Falling from {}m height".format(h))
            if h>window:
                num+=1
                print("Ball can be seen")
            h=bounce*h
            print("Bouncing to {}m height".format(h))
            if h>window:
                num+=1
                print("Ball can be seen")            
            else:
                return num
        
print("result:",bouncingBall(3,0.66,1.5))
print(30*'-')
print("result:",bouncingBall(30,0.66,1.5))
