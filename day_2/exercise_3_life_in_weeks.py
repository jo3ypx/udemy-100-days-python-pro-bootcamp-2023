age = input("What is your current age?\n")
age_till_90 = 90 - int(age)
days = age_till_90 * 365
weeks = age_till_90 * 52
months = age_till_90 * 12
print("You have " + str(days) + " days, " + str(weeks) +
      " weeks" + ", and " + str(months) + " months left.")
