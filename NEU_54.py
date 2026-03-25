# binary search

from jovian.pythondsa import evaluate_test_case
from jovian.pythondsa import evaluate_test_cases


liste_rot = [5, 6, 9, 0, 2, 3, 4]

def rot_fkt(liste, anzahl_rot):
    if min(liste) == liste[0]:
        return 0
    else:
        k = [0] * len(liste)
        for i in range(len(liste)):
            k[i] = liste[i-anzahl_rot]
        return k

print(rot_fkt(liste_rot, 4))




liste_rot = [5, 6, 9, 0, 2, 3, 4]

def rot_fkt(liste):
   n = 0
   if liste[0] == 0:
    return n
   else:
        while min(liste) != liste[0]:
            k = [0] * len(liste)
            for i in range(len(liste)):
                k[i] = liste[i-1]
            liste = k
            n += 1
        return n

print(rot_fkt(liste_rot))

liste_blau = [0, 2, 3, 4, 5, 6, 9]


# RECHTSRUM rotieren
print('-------------- RECHTSRUM ----------------')


def count_rotations_rechts(nums):
   rotations = 0
   while min(nums) != nums[0]:
        k = [0] * len(nums)
        for i in range(len(nums)):
            k[i] = nums[i-1]
        nums = k
        rotations += 1
   return rotations

print(count_rotations_rechts(liste_blau), count_rotations_rechts(liste_rot))

# LINKSRUM rotieren
print('-------------- LINKSRUM ----------------')

def count_rotations(nums):
   rotations = 0
   while min(nums) != nums[0]:
        k = [0] * len(nums)
        for i in range(len(nums)-1):
            k[i] = nums[i+1]
        k[len(nums)-1] = nums[0]
        nums = k
        rotations += 1
   return rotations

print(count_rotations(liste_blau), count_rotations(liste_rot))

test = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}

print(evaluate_test_case(count_rotations, test))

# zwei Listen zu einer zusammengepackt
liste_test = [3,4,5,6]
liste_dazu = [7,8,9]

liste_zsm = [*liste_test, *liste_dazu]

test0 = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}


test1 = {
    'input': {
        'nums': [4, 5, 6, 7, 8, 1, 2, 3]
    },
    'output': 5
}

test2 = {
    'input': {
        'nums': [3, 5, 6, 7, 9, 11, 14, 19, 25, 29]
    },
    'output': 0
}

test3 = {
    'input': {
        'nums': [40, 3, 5, 6, 7, 9, 11, 14, 19, 25, 29]
    },
    'output': 1
}

test4 = {
    'input': {
        'nums': [5, 6, 7, 9, 11, 14, 19, 25, 29, 3]
    },
    'output': 9
}

test5= {
    'input': {
        'nums': [3, 5, 6, 7, 9, 11, 14, 19, 25, 29]
    },
    'output': 0
}

test6= {
    'input': {
        'nums': []
    },
    'output': 0
}

test7= {
    'input': {
        'nums': [3]
    },
    'output': 0
}
tests = [f"test{i}" for i in range(7)]
print("---")
print(tests)
print("'''''''''''''")


tests_k = [test0, test1, test2, test3, test4, test5, test6, test7]
tests = [test0, test1, test3, test5]

print(evaluate_test_cases(count_rotations, tests))

print(test4["input"]["nums"])
print("+++")
def differenz(nums):
    verschobene_liste = [nums[-1]] + nums[:-1]
    ergebnis = [a - b for a, b in zip(verschobene_liste, nums)]
    position = [i for i, val in enumerate(ergebnis) if val > 0]
    rotations = position[0]
    return rotations


list_tesst = [2,3,4,5,1]
print(differenz(list_tesst))

print('11111111111')
print(evaluate_test_cases(count_rotations, tests))
print("2222222222222222")
print(evaluate_test_cases(differenz, tests))

def count_rotations_linear(nums):
    position = 0

    while position < len(nums):
        if position > 0 and nums[position] < nums[position-1]:
            return position

        position += 1

    return 0

print("33333333333333")
print(evaluate_test_cases(count_rotations_linear, tests))

print("44444444444")
list_links = [5,1,2,3,4]
list_rechts = [2,3,4,5,1]
list_tst = [3,4,5,1,2]
list_o = [1,2,3,4,5]
list_list = [4,5,1,2,3]
def count_rotations_linear2 (nums):
    lo, hi = 0, len(nums)-1
    while lo < hi:
        mitte = (lo + hi) // 2
       # print(lo, mitte, hi)
        if nums[mitte] < nums[mitte-1]:
            return mitte
        elif(nums[lo] < nums[mitte]) and (nums[mitte] < nums[hi]):
            return 0
        elif  nums[mitte] < nums[hi]:
            hi = mitte - 1
        else:
            lo = mitte + 1

    return lo

print(count_rotations_linear2(list_links))
print(count_rotations_linear2(list_rechts))
print(count_rotations_linear2(list_tst))
print(count_rotations_linear2(list_o))
print(count_rotations_linear2(list_list))

print("TTTTTEEEEEESSSSSSTTTTTT")
print(evaluate_test_cases(count_rotations_linear2, tests_k))









