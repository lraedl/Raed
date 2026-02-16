import itertools

def task1_fast():
    letters_without_g = ['Е', 'П', 'А', 'Р', 'Д']
    count = 0
    
    for g_pos in range(5):
        for other in itertools.product(letters_without_g, repeat=4):
            word_list = list(other)
            word_list.insert(g_pos, 'Г')
            word = ''.join(word_list)
            
            if word[0] != 'А' and word[4] != 'Е':
                count += 1
    
    return count

print("\nЗадача 1:", task1_fast())