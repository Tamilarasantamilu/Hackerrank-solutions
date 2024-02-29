def merge_the_tools(string, k):
    new_str = ''
    for i in range (0, len(string), k):
        for letter in string[i:i+k]:
            if letter not in new_str:
                new_str = new_str + letter
        print(new_str)
        new_str = ''
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)