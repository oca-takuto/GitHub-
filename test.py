def main():
    print('Hello Python')
<<<<<<< HEAD
    print('+--------------------------------------------+')
    for i in range(1,10):
        
        print(end="|")
        for j in range(1,10):
            if i*j < 10:
                print(" ",i*j,end=" |")
            else:
                print("",i*j,end=" |")
        print('\n+--------------------------------------------+')


if __name__=='__main__':
