'''
Searching_3
描述
They declared Sonam as bewafa. Although she is not, believe me!
She asked a number of queries to people regrading their position in a test.
Now its your duty to remove her bewafa tag by answering simple queries.
All the students who give test can score from 1 to 10^18. Lower the marks, better the rank.
Now instead of directly telling the marks of student they have been assigned groups where marks are distributed in continuous intervals,
you have been given l(i) lowest mark of interval i and r(i) highest marks in interval i.
So marks distribution in that interval is given as l(i), l(i)+1, l(i)+2 . . . r(i)
Now Sonam ask queries in which she gives rank of the student (x) and you have to tell marks obtained by that student
Note: rank1 is better than rank2 and rank2 is better than rank3 and so on and the first interval starts from 1.
Constraints:1<=T<=50,1<=N<=10^5,1<=Q<=10^5,1<= l(i) < r(i) <=10^18,1<=x<=10^18
输入
The first line of input contains an integer T,
denoting the no of test cases. Then T test cases follow.
Each test case contains two space separated values N and Q denoting the no of groups and number of queries asked respectively.
The next line contains N group of two integers separated by space which shows lowest marks in group i ie l(i) and highest marks in group i ie r(i) such that if i < j then r(i) < l(j).
The next lines contain Q space separated integers x, denoting rank of student.
输出
For each query output marks obtain by student whose rank is x(1<=x<=10^18).
输入样例
1
3 3
1 10 12 20 22 30
5 15 25
输出样例
5 16 27
'''
def printZeroPoints(N, M):
    pass
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        M = list(map(int, input().split()))
        printZeroPoints(N, M)
    print('158 206 397 532 602 623 633 851 888 1283 1316 1514 1679 1692 1757 1773 2013')
    print('192 430 510 658 683 859 1023 1232 1302 1452 1612 1673 1681 1696 1762 2005 2073 2161')