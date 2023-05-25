def bubble_sort(arr):
    n = len(arr)

    # 遍历数组元素
    for i in range(n):
        # 每次遍历找到当前未排序部分的最大元素，并将其放置到正确的位置
        for j in range(0, n - i - 1):
            # 如果当前元素大于下一个元素，则交换它们的位置
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# 测试示例
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("排序后的数组：")
for i in range(len(arr)):
    print(arr[i], end=" ")
