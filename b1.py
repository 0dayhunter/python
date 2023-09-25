def TOH(n, src, dest, middle):
    if n == 1:  
        print("Move disk 1 from", src, "to", dest)
        return
    TOH(n - 1, src, middle, dest)
    print("Move disk", n, "from", src, "to", dest)
    TOH(n - 1, middle, dest, src)

N = int(input("How many disks do you have: "))  
TOH(N, 'A', 'C', 'B')
