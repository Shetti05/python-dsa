def rotate_array(nums, k):
    k = k % len(nums)
    return nums[-k:] + nums[:-k]


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print("Rotated Array:", rotate_array(arr, k))
