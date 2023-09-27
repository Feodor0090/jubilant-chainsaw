def ask_list():
    print("Введите числа через пробелы:", end='')
    return [int(i) for i in input().split()]


def bucket_sort(arr):
    max_value = max(arr)
    size = max_value / len(arr)

    # buckets count = elements count
    buckets = [[] for _ in range(len(arr))]

    # putting objects into each bucket by value
    for i in range(len(arr)):
        j = int(arr[i] / size)
        if j != len(arr):
            buckets[j].append(arr[i])
        else:
            buckets[len(arr) - 1].append(arr[i])

    # Sort elements within the buckets using insertion Sort
    for z in range(len(arr)):
        insertion_sort(buckets[z])

    # concatenate buckets into a single list
    final_output = []
    for x in range(len(arr)):
        final_output = final_output + buckets[x]
    return final_output


def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        var = bucket[i]
        j = i - 1
        while j >= 0 and var < bucket[j]:
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var


if __name__ == '__main__':
    try:
        with open('input') as f:
            lst = [int(i) for i in f.readline().split()]
    except:
        lst = ask_list()
    sorted = bucket_sort(lst)
    print(sorted)
    try:
        with open('output', 'w') as o:
            o.write(str(sorted))
    except:
        print('No output file found')
