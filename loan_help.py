ALL_LOANS_DICT = {'direct_unsub_0':[1060.98, 0.06600],
                  'direct_unsub_1': [5319.57, 0.06000],
                  'direct_unsub_2': [2234.94, 0.04290],
                  'direct_unsub_3': [2365.74, 0.04660],
                  'direct_unsub_4': [2362.65, 0.03860],
                  'direct_unsub_5': [2910.10, 0.06800],
                  'direct_sub_6': [5449.22, 0.04290],
                  'direct_sub_7': [5469.33, 0.04660],
                  'direct_sub_8': [4525.49, 0.03860],
                  'direct_sub_9': [3495.70, 0.03400]
                  }

def getIntPerYear(loan):
    ''' loan is a tuple, where the first item is the balance and the second item is the interest rate '''

    return round(loan[0]*loan[1], 2)

def getIntPerMonth(loan):
    ''' loan is a tuple, where the first item is the balance and the second item is the interest rate '''

    return round((loan[0]*loan[1]) / 12, 2)

def getIntPriorityDict(loans_dict):
    ''' return a dictionary, where the key is the name of the loan and the value is the result of the loan balance times the interest rate (to give the total interest that will accrue in a year) '''

    dict_of_interest = {}
    for k, v in loans_dict.items():
        dict_of_interest[k] = getIntPerYear(v)

    return dict_of_interest

def getPriorityDict(dict_of_interest):
    ''' the argument is a dictionary where the key is the name of the loan and the value is the amount of interest to be paid during 1 year || the function will return an ordered list of which of the
    loans are higher priorities, where the item of the list will be the name of the loan '''

    prioritized = []
    for k, v in sorted(dict_of_interest.items(), key=lambda item: item[1]):
        prioritized.append(k)

    return list(reversed(prioritized))

def getTotalOwed(loans_dict):
    ''' returns the total amount owed currently, based on the balance and not the interest '''

    owed = 0

    for k, v in loans_dict.items():
        owed += loans_dict[k][0]

    return round(owed, 2)

def addInterestToLoans(loanExcused, loans_dict):
    ''' ignores loans that are decremented that month, and adds compounds interest on other loans monthly '''


    for loan, loan_tuple in loans_dict.items():
        if loan in loanExcused:
            continue
        else:
            intToAdd = getIntPerMonth(loan_tuple)
            loan_tuple[0] += intToAdd

def getOrderedList():

    totalOwed = getTotalOwed(ALL_LOANS_DICT)
    monthlyPayment = 1000
    month = 0
    orderedList = []

    while totalOwed > 0:
        dictOfLoanInt = getIntPriorityDict(ALL_LOANS_DICT) # dictionary key = loan name, value = balance*interest
        loanListPriority = getPriorityDict(dictOfLoanInt) # ordered list of which loan to pay first
        loansPaid = []

        for i in loanListPriority:
            balance, interest = ALL_LOANS_DICT[i]
            loansPaid.append(i)
            balance -= monthlyPayment
            ALL_LOANS_DICT[i] = [balance, interest]
            if balance < 0:
                monthlyPayment = balance * -1
            else:
                break

        totalOwed -= 1000
        monthlyPayment = 1000
        month += 1
        orderedList.append(loansPaid)
        addInterestToLoans(loansPaid, ALL_LOANS_DICT)

    return orderedList

order = getOrderedList()
for i in enumerate(order, start=1):
    print(i)







# prior = getIntPriorityDict(ALL_LOANS_DICT)
# print(prior)
# print('\n')
# print(getPriorityDict(prior))
#
# addInterestToLoans(['direct_unsub_1', 'direct_unsub_4'], ALL_LOANS_DICT)
# print('\n')
# print(ALL_LOANS_DICT)
