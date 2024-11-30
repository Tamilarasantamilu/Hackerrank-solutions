 minion_game(string):
    vowels = 'AEIOU'
    kevin_scores = stuart_scores = 0
    length = len(string)
    for i in range(length):
        if string[i] in vowels:
                kevin_scores += length - i
        else:
            stuart_scores += length - i
    if stuart_scores > kevin_scores:
        print(f'Stuart {stuart_scores}')
    elif kevin_scores > stuart_scores:
        print(f'Kevin {kevin_scores}')
    else:
        print ('Draw')
    # your code goes here

if __name__ == '__main__':
    s = input()
    minion_game(s)
#end code
#end