if __name__ == '__main__':
    N = int(input())
    lst = []
    for item in range(N):
        cmd = input().split()
        if cmd[0] == 'insert':
            lst.insert(int(cmd[1]), int(cmd[2]))
        if cmd[0] == 'print':
            print(lst)
        if cmd[0] == 'remove':
           lst.remove(int(cmd[1]))
        if cmd[0] == 'append':
            lst.append(int(cmd[1]))
        if cmd [0]== 'sort':
            lst.sort()
        if cmd[0] == 'pop':
            lst.pop()
        if cmd[0] == 'reverse':
            lst.reverse()
            #end of the code
