ALL_LOANS_DICT = {'direct_unsub_0':[1055.70, 0.06600],
                  'direct_unsub_1': [3364.79, 0.06000],
                  'direct_unsub_2': [2229.49, 0.04290],
                  'direct_unsub_3': [2362.97, 0.04660],
                  'direct_unsub_4': [2353.46, 0.03860],
                  'direct_unsub_5': [2910.1, 0.06800],
                  'direct_sub_6': [5436.03, 0.04290],
                  'direct_sub_7': [5462.96, 0.04660],
                  'direct_sub_8': [4507.91, 0.03860],
                  'direct_sub_9': [3476.64, 0.03400]
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

def addInterestToLoans(loans_dict):
    ''' ignores loans that are decremented that month, and adds compounds interest on other loans monthly '''
    
    totalInterest = 0

    for loan, loan_tuple in loans_dict.items():
        intToAdd = getIntPerMonth(loan_tuple)
        totalInterest += intToAdd
        loan_tuple[0] += intToAdd
        
    return totalInterest
        

def getOrderedList():

    totalOwed = getTotalOwed(ALL_LOANS_DICT)
    monthlyPayment = 400
    month = 0
    orderedList = []
    interestAccrued = 0

    while totalOwed > 0:
        interestAccrued += addInterestToLoans(ALL_LOANS_DICT)
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

    print(interestAccrued)
    return orderedList

order = getOrderedList()
for i in enumerate(order, start=1):
    print(i)
