'''
栈
'''
import sys
def process(curAct, startStack, endStack):
    global record
    if ((len(startStack) != 0 and abs(record) != abs(curAct)) and (len(endStack) == 0 or startStack[len(startStack) - 1] < endStack[len(endStack) - 1])):
        endStack.append(startStack.pop())
        # if curAct == 1:
        #     print("l->m")
        # elif curAct == -1:
        #     print("m->l")
        # elif curAct == 2:
        #     print("r->m")
        # elif curAct == -2:
        #     print("m->r")
        record = curAct
        return 1
    return 0
def hanoi(num):
    lStack = []
    mStack = []
    rStack = []
    lStack.append(sys.maxsize)
    mStack.append(sys.maxsize)
    rStack.append(sys.maxsize)
    i = num
    while(i > 0):
        lStack.append(i)
        i -= 1
    steps = 0
    while(len(rStack) != num + 1):
        steps += process(1, lStack, mStack)
        steps += process(-1, mStack, lStack)
        steps += process(2, rStack, mStack)
        steps += process(-2, mStack, rStack)
    return steps
if __name__ == '__main__':
    n = int(input())
    record = 0
    print(hanoi(n))