prev_mean = 38
total = 40
wrong_num = 36
right_num = 56

sum = prev_mean * total
print("sum of 40 numbers:",sum)

correct_sum = sum - wrong_num + right_num
print("correct sum",correct_sum)

correct_mean = correct_sum/total
print("correct mean",correct_mean)