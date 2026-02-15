def count_subarrays_with_xor(arr, target):
    xor_map = {0: 1}
    current_xor = 0
    count = 0

    for num in arr:
        current_xor ^= num
        needed = current_xor ^ target

        if needed in xor_map:
            count += xor_map[needed]

        xor_map[current_xor] = xor_map.get(current_xor, 0) + 1

    return count


if __name__ == "__main__":
    arr = [4, 2, 2, 6, 4]
    target = 6
    print("Count:", count_subarrays_with_xor(arr, target))
