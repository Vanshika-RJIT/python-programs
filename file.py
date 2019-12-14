with open("vanshika.txt") as f:
    print(f.read(4))
    print(f.tell())
    print(f.read(9))
    print(f.read(4))
    f.seek(0)
    print(f.read(10))
    f.seek(0)
    for line in f:
        print(line,end='')
    f.seek(0)
    print(f.readline())
    print(f.readline())
    print(f.readlines())
    
    
    

