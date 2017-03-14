def fine_print(n):
    
    print("dec:{0:6} oct:{0:8} hex:{0:8} bin: \n".format(" "))

    for i in range(1, n+1):
        print("{0:<10d} 0o{0:<10o} 0x{0:<10X} 0b{0:<10b}".format(i))

    return True


if __name__ == "__main__":

    n = int(input("Input N :"))

    fine_print(n)