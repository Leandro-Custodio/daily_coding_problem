
def bubbleSort(arr, k):
    result = False
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            print("_______________")
            print(str(arr[i]) + " + " + str(arr[j]))
            print("_______________")
            print("result = " + str(arr[j] + arr[i]))
            print(" ")
            if arr[j] + arr[i] == k:
                result = True
    print ("The result is " + str(result))
    return bool(result)

def automated_testing(arr,k):
    print("Start Automated testing")
    test_valid = bubbleSort(arr, k)
    print("Finish Automated testing")
    if test_valid == False:
        print ("Test Failed - Error no Method ")
        print ("consult https://github.com/Leandro-Custodio/daily_coding_problem Problem-#01")
    else:
        print ("Test Valid - :D ")
        print(" ")

automated_testing([10, 15, 3, 7], 17)

arr = []
run_again = True
while run_again:
    quant = int(input("insert how many elements you want: "))
    for i in range(0, quant):
        arr.append(int(input("Enter next no : ")))
    k = int(input("What's your K "))
    print("your list number is : "+ str(arr))
    print("your k number is : " + str(k))
    confirm = input("confirm ? yes or not ")
    if confirm == "yes":
        run_again = False
bubbleSort(arr, k)
