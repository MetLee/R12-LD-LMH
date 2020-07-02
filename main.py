import itertools
import wordninja

ARCHETYPES = ['Dreamer', 'Visionary', 'Interpreter', 'Trickster','Spiritualist', 'Patron', 'Humanist', 'Ominescent', 'Listener', 'Explorer', 'Skeptic', 'Catalyst', 'Alchemist']

INDICES_OF_PASSCODE = [[1,1,25,7], [9,1,15,8], [7,1,19,2], [4,2,18,9], [11,2,21,6], [14,6,27,3], [13,6,16,1], [5,4,26,5], [8,3,20,4], [3,4,17,5], [6,4,24,5], [2,6,22,9], [12,2,23,1]]

DEFAULT_POSITIONS = [7, 0, 0, 0, 1, 0, 0, 0, 6, 11, 13, 8, 2]

def exclude():
    archetypes_temp = ARCHETYPES.copy()
    for i in range(len(DEFAULT_POSITIONS)):
        if DEFAULT_POSITIONS[i]:
            archetypes_temp[i] = ''
    try:
        while True:
            archetypes_temp.remove('')
    except:
        return archetypes_temp

def get_permutations():
    permutations = []
    archetypes_exclude = exclude()
    permutations_exclude = list(itertools.permutations(archetypes_exclude))
    for permutation_exclude in permutations_exclude:
        permutation_exclude_temp = list(permutation_exclude)
        permutation = [0] * len(ARCHETYPES)
        for i in range(len(DEFAULT_POSITIONS)):
            if DEFAULT_POSITIONS[i]:
                permutation[DEFAULT_POSITIONS[i] - 1] = ARCHETYPES[i]
        for i in range(len(permutation)):
            if not permutation[i]:
                permutation[i] = permutation_exclude_temp.pop(0)
        permutations.append(permutation)
    return permutations
 
def get_code(permutation):
    code = [0] * 27
    code[9] = 'w'
    for i in range(len(INDICES_OF_PASSCODE)):
        try:
            code[INDICES_OF_PASSCODE[i][0] - 1] = permutation[i][INDICES_OF_PASSCODE[i][1] - 1]
            code[INDICES_OF_PASSCODE[i][2] - 1] = permutation[i][INDICES_OF_PASSCODE[i][3] - 1]
        except:
            return ''
    return ''.join(code)
     
def main():
    rst = []
    permutations = get_permutations()
    for permutation in permutations:
        code = get_code(permutation)
        if code:
            rst.append([code, len(wordninja.split(code))])
    rst.sort(key=lambda x: x[1])
    print(rst[:10])
    
if __name__ == '__main__':
    main()