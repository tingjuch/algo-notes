# String S of N digits as a number, 
# you can change at most 1 digit such that S can be divide by 3.
# Write a function to return how many possibilities.

def solution(S):
    nums = [int(c) for c in S]
    all_sum = sum(nums)

    actual = 0
    for n in nums:
        others_sum = all_sum - n
        if others_sum % 3 == 0:
            actual += 3 if n in [0,3,6,9] else 4
        elif others_sum % 3 == 1:
            actual += 2 if n in [2,5,8] else 3
        else:
            actual += 2 if n in [1,4,7] else 3
    if all_sum % 3 == 0:
        actual += 1

    possibilities = set()
    for i, n in enumerate(nums):
        others_sum = all_sum - n
        if others_sum % 3 == 0:
            alternatives = ["0","3","6","9"]
        elif others_sum % 3 == 1:
            alternatives = ["2", "5", "8"]
        else:
            alternatives = ["1", "4", "7"]

        for x in alternatives:
            p = S[:i] + x + S[i+1:]
            possibilities.add(p)
    expected = len(possibilities)
    
    print(actual, expected)


for q in ["23", "0081", "022", "369", "345636", "1991", "0005167", "135872", "00016278", "00029380129830120398012983"]:
    solution(q)