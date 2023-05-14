H, W = map(int, input().split())
height = list(map(int, input().split()))

def check():
    rain = 0
    left, right = 0, W - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(left_max, height[left]), max(right_max, height[right])

        if left_max <= right_max:
            rain += left_max - height[left]
            left += 1
        else:
            rain += right_max - height[right]
            right -= 1

    return rain


print(check())
