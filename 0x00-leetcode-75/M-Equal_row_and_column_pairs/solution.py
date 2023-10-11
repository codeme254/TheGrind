from typing import List
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows_hash = {}
        total_pairs = 0
        for row in grid:
            current_str = "#".join(map(str, row))
            if not rows_hash.get(current_str):
                rows_hash[current_str] = 1
            else:
                rows_hash[current_str] += 1
        
        length = len(grid[0])
        i = 0
        while i < length:
            current_str_arr = []
            for row in grid:
                current_str_arr.append(row[i])
            current_str = "#".join(map(str, current_str_arr))
            
            if rows_hash.get(current_str):
                total_pairs += rows_hash[current_str]
            i += 1
        return total_pairs

s = Solution()
print(s.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))