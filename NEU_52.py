from jovian.pythondsa import evaluate_test_case, binary_search
from jovian.pythondsa import evaluate_test_cases

# an welcher stelle ist eine bestimmte zahl in liste?

liste = [13, 11, 10, 7, 4, 3, 1, 0]
def locate_card(cards, query):
    k = 0
    for i in cards:
        if i != query:
            k += 1
        else:
            break
    return k

print(locate_card(liste, 7))

test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

print(locate_card(**test['input']) == test['output'])

tests = []
tests.append(test)
tests.append({
'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

tests.append({
'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

tests.append({
'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

tests.append({
'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0
})

tests.append({
'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

tests.append({
'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

tests.append({
'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

tests.append({
'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})

print(tests)
print("--------------")
def locate_card_2(cards, query):
    if query not in cards:
        return -1
    if len(cards) == 0:
        return -1
    pos = 0
    print('cards:', cards)
    print('query:', query)

    while True:
        print('position:', pos)

        if cards[pos] == query:
            return pos

        pos += 1

        if pos == len(cards):
            return -1

print("+++++")
result = locate_card_2(test['input']['cards'], test['input']['query'])

print("MMMMM")
print(result == test['output'])

print("*****")
evaluate_test_case(locate_card_2, test)

print("HHHHH")
for test in tests:
    print(locate_card(**test['input']) == test['output'])

print("----")
print(evaluate_test_cases(locate_card_2, tests))
print(44444)
def locate_card_3(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

print(tests[5])

print("---------")
print(locate_card_3([], 7))

print(evaluate_test_cases(locate_card_3, tests))
print("NNNNNNNEEEEEE")
# zb 9 7 5 4 3 2 1
def locate_card_4(cards, query):
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]
        print("lo:", lo, "hi:", hi, "mid:", mid,
              "mid_number:", mid_number)
        if cards[mid] == query:
            return mid
        elif cards[mid] < query:
            hi = mid - 1
        elif cards[mid] > query:
            lo = mid + 1

    return - 1

print(evaluate_test_cases(locate_card_4, tests))




print('-----------g-----------')
print(evaluate_test_case(locate_card_4, tests[8]))


def test_location(cards, query, mid):
    mid_number = cards[mid]
   # print("mid:", mid, ". mid_number:", mid_number)
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
       # print("lo:", lo, "hi:", hi)
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid -1
        elif result == 'right':
            lo = mid + 1
    return -1


print(evaluate_test_case(locate_card, tests[8]))


# linear extrem test case

def locate_card_linear(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

large_test = {
    'input': {
        'cards': list(range(10000000, 0, -1)),
        'query': 2
    },
    'output': 9999998

}

result, passed, runtime = evaluate_test_case(locate_card_linear, large_test, display=False)
print(f"RESULT {result}, PASSED {passed}, RUNTIME {runtime}")

print("_________________")
result, passed, runtime = evaluate_test_case(locate_card, large_test, display=False)
print(f"RESULT {result}, PASSED {passed}, RUNTIME {runtime}")


def test_location(cards, query, mid):
    mid_number = cards[mid]
   # print("mid:", mid, ". mid_number:", mid_number)
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'


print("iiiiiiiiiiiiiiiiiii")
def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) //2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

def locate_card(cards, query):

    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid - 1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'


    return binary_search(0, len(cards) - 1, condition)

print(evaluate_test_cases(locate_card, tests))
print(333)
def first_position(nums, target):

    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid - 1] == target:
                return 'left'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums) - 1, condition)

def last_position(nums, target):

    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid + 1] == target:
                return 'right'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums) - 1, condition)

def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)

