class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        if len(bank) == 1:
            return 0
        left_pointer = 0
        right_pointer = 1
        total_beams = 0
        while right_pointer < len(bank):
            row1 = bank[left_pointer]
            row2 = bank[right_pointer]
            if self.has_security_device(row2):
                total_beams += self.num_beams_between_two_rows(row1, row2)
                temp = right_pointer
                right_pointer += 1
                left_pointer = temp
            else:
                right_pointer += 1
        return total_beams

    def num_beams_between_two_rows(self, left_row, right_row):
        """
        Counts the number of beams between two rows
        """
        devices_in_right_row = self.count_security_devices(right_row)
        if devices_in_right_row == 0:
            return 0
        
        total_beams = 0
        for i in range(0, len(left_row)):
            if left_row[i] == "1":
                total_beams += devices_in_right_row
        return total_beams
    
    def count_security_devices(self, row):
        """
        counts the number of security devices in a row
        """
        number_of_devices = 0
        for i in range(0, len(row)):
            if row[i] == "1":
                number_of_devices += 1
        return number_of_devices

    def has_security_device(self, row):
        """
        checks if there is a security device in a given floor row
        :row - a string made up of 0s or 1s or both
        0 denotes no security device, 1 denotes a security device
        returns True if there is a security device and false if there is not
        """
        for i in range(0, len(row)):
            if row[i] == '1':
                return True
        return False

s = Solution()
print(s.numberOfBeams(["01", "00", '00', "00", '00', "01", "01", "01"]))
