'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, curr_index=0, th_count=0):
    word_list = list(word)

    if len(word) <= 1: 
        return 0

    elif(curr_index >= len(word_list)-1):
        return(th_count)

    elif(word_list[curr_index] == 't' and word_list[curr_index+1] == 'h'):
        th_count += 1 
        curr_index += 1 
        return count_th(word, curr_index, th_count)

    else: 
        curr_index += 1
        return count_th(word, curr_index, th_count)
