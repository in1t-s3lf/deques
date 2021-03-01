from collections import deque

stack= deque(maxlen=100)
ext=False
while(ext==False):
    cmd=input()
    if(cmd[:10]=='push_front'):
        stack.appendleft(cmd[11:])
        print('ok')
    elif(cmd[:9]=='push_back'):
        stack.append(cmd[10:])
        print('ok')
    elif(cmd[:3]=='pop' or cmd=='front'or cmd=='back'):
        if(len(stack)>=1):
            if(cmd=='pop_front'):
                print(stack.popleft())
            elif(cmd=='pop_back'):
                print(stack.pop())  
            elif(cmd=='front'):
                print(stack[0])
            elif(cmd=='back'):
                print(stack[-1]) 
        else: print('error')
    elif(cmd=='size'):
        print(len(stack))
    elif(cmd=='clear'):
        stack.clear()
        print('ok')
    elif(cmd=='exit'):
        print('bye')
        ext=True
