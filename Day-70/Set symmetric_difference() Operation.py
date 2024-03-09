def total_students(subscribed_english, subscribed_french):
    english_set = set(subscribed_english)
    french_set = set(subscribed_french)
    
    not_both_subscribed = english_set.symmetric_difference(french_set)
    
    return len(not_both_subscribed)

english_count = int(input())
english_students = input().split()
french_count = int(input())
french_students = input().split()

print(total_students(english_students, french_students))
