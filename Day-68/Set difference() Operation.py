n_eng = int(input())
eng_roll_numbers = set(map(int, input().split()))
n_french = int(input())
french_roll_numbers = set(map(int, input().split()))

only_english = eng_roll_numbers.difference(french_roll_numbers)

print(len(only_english))
