class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        partitions = 0
        for i in range(0, len(n)):
            if int(n[i]) > int(partitions):
                partitions = n[i]
        return int(partitions)

s = Solution()
print(s.minPartitions("32"))
print(s.minPartitions("82734"))
print(s.minPartitions("27346209830709182346"))
