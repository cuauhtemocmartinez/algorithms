def interest_calc(principal,years,rate): 
    print('The principal amount is', principal) 
    print('Number of years is', years) 
    print('The rate of interest is',rate) 
      
    simple_interest = (principal * years * rate)/100
      
    print('The Simple Interest is', simple_interest) 
    return simple_interest
      
interest_calc(100, 5, 4.5) 