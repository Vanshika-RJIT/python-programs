try:
    f=open("vanshikaS.txt",mode='w+')
    f.write('vanshika sikarwar is a good girl\n')
    f.write('she is always trying to keep it up\n')
    f.seek(0)
    print(f.read())
finally:
    f.close()
    
