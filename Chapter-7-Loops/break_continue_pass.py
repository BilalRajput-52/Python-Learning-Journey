# Topic: break, continue, pass

# break Statement

# Definition:
# break immediately terminates the loop.

for i in range(1, 11):
    if i == 5:
       break
    print("break the loop immediately after five:",i)
# ==========================================

# continue Statement

# Definition:
# continue skips the current iteration and
# moves to the next iteration.
print("\n")
for i in range(1, 6):
    if i == 3:
       continue
    print("skip the 3 number then continue:",i)
# =========================================
# pass Statement

# Definition:
# pass is a null statement.
# It does nothing and is used as a placeholder.
print("\n")
for i in range(5):
    if i == 3:
       pass
    print("Do nothing follow same flow of numbers:",i)

# Easy Real-Life Example

# Socho tum class me ho:

# break = Teacher ne kaha: "Class khatam, sab ghar jao."
# continue = Teacher ne kaha: "Bilal ko skip karo, baki sab attendance do."
# pass = Teacher ne kuch nahi kaha, class normal chalti rahi.
# One-line Memory Trick
# break → Stop the loop.
# continue → Skip current iteration.
# pass → Do nothing.