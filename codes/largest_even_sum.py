# A: array of N positive numbers
# K: positive integer
# Find largest even sum when selecting K numbers in A with distinct positions

def solution(A, K):
    
    odds = []
    evens = []

    for n in sorted(A, reverse=True):
        if n % 2 != 0:
            odds.append(n)
        else:
            evens.append(n)
    
    max_sum = -1
    for n_odd in range(0, K+1, 2):
        n_even = K - n_odd
        if n_odd > len(odds) or n_even > len(evens):
            continue
        max_sum = max(max_sum, sum(odds[:n_odd] + evens[:n_even]))
    print(max_sum)


solution([4,9,8,2,6], 3)
solution([5,6,3,4,2], 5)
solution([7,7,7,7,7], 1)
solution([10000], 2)
solution([2,3,3,5,5], 3)