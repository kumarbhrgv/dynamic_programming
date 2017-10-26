def countCoinChange(arr, length, total):
    combinations = [[0 for y in range(length)] for y in range(total+1)]
    for x in range(length):
        combinations[0][x] = 1
    for i in range(1, total+1):
        for j in range(length):
            x = combinations[i - arr[j]][j] if i-arr[j] >= 0 else 0
            y = combinations[i][j-1] if j >= 1 else 0
            combinations[i][j] = x + y
    return combinations[total][length-1]

if __name__ == "__main__":
    arr = [10,5,1]
    coin_to_be_changed = 10
print("Denominations for coin with cents : ", coin_to_be_changed,"=",countCoinChange(arr, length, coin_to_be_changed))
