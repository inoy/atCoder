for i in range(10000):
    xxx = 0.9
    a = i ** xxx
    # print(a)
    if str(a).split(".")[1] == "0":
        print(i)
