class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        paper_time = self.time_to_collect_garbage("P", garbage, travel)
        glass_time = self.time_to_collect_garbage("G", garbage, travel)
        metal_time = self.time_to_collect_garbage("M", garbage, travel)
        return paper_time + glass_time + metal_time
    
    def time_to_collect_garbage(self, garbage_type, garbage, travel):
        """
        Returns the total amount of time needed to collect certain type of garbage
        :garbage_type: the type of garbage, "M", "P", "G"
        :houses: an array of houses with the garbages
        :travel: times it take to move from one house to another
        """
        current_garbage = 0
        look_ahead = 0
        current_travel_time = 0
        time = 0
        temp_time = 0
        while current_garbage < len(garbage):
            if self.count_garbage(garbage_type, garbage[current_garbage]) > 0:
                time += self.count_garbage(garbage_type, garbage[current_garbage]) * 1 + temp_time
                temp_time = 0
            # else:
            if current_travel_time < len(travel):
                temp_time += travel[current_travel_time]
            current_travel_time += 1
            current_garbage += 1
        return time
                
    def count_garbage(self, garbage_type, garbage):
        """
        Counts the amount of certain garbage in a given garbage
        """
        total = 0
        for i in range(0, len(garbage)):
            if garbage[i] == garbage_type:
                total += 1
        return total

s = Solution()
print(s.garbageCollection(["G","P","GP","GG"], [2,4,3]))
print(s.garbageCollection(["MMM","PGM","GP"], [3, 10]))