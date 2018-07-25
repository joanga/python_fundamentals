
def taxes_owed(brackets_u, income):
    unsorted_bracket = brackets_u
    brackets = list(sorted(unsorted_bracket))
    taxes_total = 0

    low = brackets[0]
    middle = brackets[1]
    high = brackets [2]

    low_cut = low[0]
    middle_cut = middle[0]
    high_cut = high[0]

    low_rate = low[1]
    middle_rate = middle[1]
    high_rate = high[1]

    if income <= low_cut:
        taxes_total = income * low_rate
        print ('test_1')
    elif income <= middle_cut and income < high_cut:
        middle_income = income - low_cut
        taxes_total = (middle_income * middle_rate) + (low_cut * low_rate)
        print ('test_2')
    elif income >= high_cut:
        middle_income = middle_cut - low_cut
        high_income = income - middle_cut
        taxes_total = (low_cut * low_rate) + (middle_income * middle_rate) + (high_income * high_rate)
        print ('test_3')

    return taxes_total

x = taxes_owed([(100000, 0.10), (50000, 0.08), (150000, 0.15)], 10000)
print (x)
