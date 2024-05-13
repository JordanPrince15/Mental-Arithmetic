import random
j = random.randint(0,3)
a = random.randint(-5,5)
b = random.randint(-5,5)
c = ['*', '+', '-', '/']

def Random(x,y):
    f = c[j] # This is the list of all the numerical opperators
    count = 0
    while True:
        print(x,f,y)
        for i in range(0,5):
            if f == '+':
                ans = int(input('x + y: ')) # Checks if the sum is '+'
                if ans == (x + y):
                    print('correct!')
                    count += 1
        for i in range(0,5):
            if f == '-':
                ans = int(input('x - y: ')) # Checks if the sum is '-'
                if ans == (x - y):
                    print('correct!')
                    count += 1
        for i in range(0, 5):
            if f == '/':
                ans = int(input('x / y: ')) # Checks if the sum is '/'
                if ans == (x / y):
                    print('correct!')
                    count += 1
        for i in range(0, 5):
            if f == '*':
                ans = int(input('x * y: ')) # Checks if the sum is '*'
                if ans == (x * y):
                    print('correct!')
                    count += 1
            
            else: print('incorrect!')
def main():
    Random(a,b)

if __name__ == '__main__':
    main()