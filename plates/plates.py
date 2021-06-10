"""
    File name: plates.py
    Author: Hayden French
    Date created: 6/9/2021
    Python Version: 3.9
"""

all_nums = []
count = 0

valid = []
invalid = []

for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            for l in range(0, 10):
                all_nums.append(str(i) + str(j) + str(k) + str(l))  # All 4 digit numbers


def get_combos(num1, num2):
    combos = {num1 / num2 if num2 != 0 else 0, num1 + num2, num1 - num2, num1 * num2}
    return list(combos)  # Returns all results from possible arithmetic operations


for num in all_nums:
    final_candidates = []
    first_candidates = get_combos(int(num[0]), int(num[1]))  # All possible values generated from first 2 digits
    for can in first_candidates:
        temp_list = get_combos(can, int(num[2]))
        for temp in temp_list:
            if temp not in final_candidates:
                final_candidates.append(temp)  # All possible values generated from first 3 digits
    if int(num[3]) in final_candidates:  # If the last digit is a candidate, we have satisfied the condition
        valid.append(num)
        count += 1
    else:
        invalid.append(num)

print("There are " + str(count) + " valid license plates " + str(10000 - count) + " invalid plates")
print("VALID: " + str(valid))
print("INVALID: " + str(invalid))
