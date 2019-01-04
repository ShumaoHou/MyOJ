'''
书本分发
描述
You are given N number of books. Every ith book has Pi number of pages.
You have to allocate books to M number of students.
There can be many ways or permutations to do so.
In each permutation one of the M students will be allocated the maximum number of pages.
Out of all these permutations, the task is to find that particular permutation in which the maximum number of pages allocated to a student is minimum of those in all the other permutations,
and print this minimum value. Each book will be allocated to exactly one student.
Each student has to be allocated atleast one book.
你有N本书。每本ith书都有Pi页数。你必须为M个学生分配书籍。可以有很多方法或排列方式。
在每个排列中，M个学生中的一个将被分配最大页数。
在所有这些排列中，任务是找到特定的排列，其中分配给学生的最大页数是所有其他排列中的页数中最少的，
并打印此最小值。每本书都将分配给一名学生。
每个学生必须至少分配一本书。
输入
The first line contains 'T' denoting the number of testcases.
Then follows description of T testcases:Each case begins with a single positive integer N denoting the number of books.
The second line contains N space separated positive integers denoting the pages of each book.And the third line contains another integer M, denoting the number of students
Constraints:1<= T <=70，1<= N <=50，1<= A [ i ] <=250，1<= M <=50，Note: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order (see explanation for better understanding)
输出
For each test case,
output a single line containing minimum number of pages each student has to read for corresponding test case.
输入样例
1
4
12 34 67 90
2
输出样例
113
'''
def isPossible(pages, N, M, cur_min):
    student = 1
    cur_sum = 0
    for i in range(N):
        if pages[i] > cur_min:
            return False
        if cur_sum + pages[i] > cur_min:
            student += 1
            cur_sum = pages[i]
            if student > M:
                return False
        else:
            cur_sum += pages[i]
    return True

def minPages(pages, N, M):
    if N < M :
        return -1
    sum = 0
    for i in range(N):
        sum += pages[i]
    start = 0
    end = sum
    result = 50 * 250 + 1
    while start <= end:
        mid = int((start + end) / 2)
        if (isPossible(pages, N, M, mid)):
            result = min(result, mid)
            end = mid - 1
        else:
            start = mid + 1
    return result

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        pages = list(map(int, input().split()))
        M = int(input())
        print(minPages(pages, N, M))