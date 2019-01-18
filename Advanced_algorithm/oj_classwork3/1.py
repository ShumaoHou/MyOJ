'''
数字重组整除问题
https://practice.geeksforgeeks.org/problems/largest-divisibility-test/0
描述
Babul’s favourite number is 17.
He likes the numbers which are divisible by 17.
This time what he does is that he takes a number N and tries to find the largest number which is divisible by 17,
by rearranging the digits.
As the number increases he gets puzzled with his own task.
So you as a programmer have to help him to accomplish his task.
Note: If the number is not divisible by rearranging the digits, then print “Not Possible”. N may have leading zeros.
输入
The first line of input contains an integer T denoting the no of test cases. Each of the next T lines contains the number N.
输出
For each test case in a new line print the desired output.
输入样例
4
17
43
15
16
输出样例
17
34
51
Not Possible
'''
import itertools

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        Input = str(input())
        numbers = [''.join(i) for i in itertools.permutations(Input)]
        numbers.sort()
        output, index = False, None
        j = len(numbers) - 1
        while j >= 0:
            if int(numbers[j]) % 17 == 0 and numbers[j][0] != '0':
                output = True
                index = j
                break
            else:
                None
            j -= 1
        if output == True:
            print(numbers[index])
        else:
            print("Not Possible")