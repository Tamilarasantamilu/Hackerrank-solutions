def print_formatted(number):
    l = len(str(bin(number)[2:]))
    for i in range (1, number+1):
        print(str(i).rjust(l) + ' ' + oct(i)[2:].rjust(l) + ' '+ hex(i)[2:].upper().rjust(l) + ' ' + bin(i)[2:].rjust(l))
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)