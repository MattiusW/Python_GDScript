def singleNumber(nums):
        unique_number = []

        if len(nums) == 1:
            return nums[0]

        unique = {i:nums.count(i) for i in nums}

        for key in unique:
            if unique[key] == 1:
                unique_number.append(key)

        return unique_number

def main():
    nums1 = [2,2,1]
    nums2 = [4,1,2,1,2]
    nums3 = [1]
    nums4 = [1,1,3,5,7,5,4,8,8]

    result1 = singleNumber(nums1)
    result2 = singleNumber(nums2)
    result3 = singleNumber(nums3)
    result4 = singleNumber(nums4)

    print(result1)
    print(result2)
    print(result3)
    print(result4)

if __name__ == "__main__":
    main()
