from typing import List
# Problem station:
# You can only pick from 0-9, form an ID of n digits, with no repetitive elemetents that exceed k in a row

def combo_of_nums(n: int, k: int) -> List[List[int]]:
    def dfs(cur_arr: List[int]) -> List[int]:
        if len(cur_arr) >= n:
            result.append(cur_arr[:])
            return
        
        for i in range(10):
            if len(cur_arr) >= k and cur_arr[-k:] == [i] * k:
                continue
            cur_arr.append(i)
            dfs(cur_arr)
            cur_arr.pop()

    result = []
    dfs([])
    return result

# print(len(combo_of_nums(4, 3)))
for arr in combo_of_nums(4, 3):
    print(arr)


# n = 3, k = 2
# eg. [0,1,2], [0,1,0], [0,2,0], [0,2,1], .., [9,8,9], etc

# n = 4, k = 3
# eg. [0,1,1,2], [4,3,3,1]