if __name__ == '__main__':
    x = input("enter first string")
    y = input("enter second string")
    x = x.strip()
    y = y.strip()
    sim = 0

    if len(x) > len(y):
        xx = x
        yy = y
    else:
        xx = y
        yy = x
    j = 0

    for i in yy:  # Changed 'in xy' to 'in yy'
        if i == xx[j]:
            sim += 1
        j += 1

    similarity = sim / len(xx)
    print("the similarity b/w the two given string is", similarity)
