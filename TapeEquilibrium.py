def solution(A):
    diff = []
    rightSum = A[0]
    leftSum = sum(A[1:])
    for i in range(0, len(A)-1):
        diff.append(abs( rightSum - leftSum ))
        leftSum -= A[i+1]
        rightSum += A[i+1]

    return min(diff)

print(solution([3,1,2,4,3]))