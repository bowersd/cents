
def early_finish_accrual(payment, final_payment_time, loan_term, inflation_rate):
    #if you pay off the loan in month n (final_payment_time), by the end of the loan term you will have accrued this much money in the currency of the time when you paid off the loan
    return sum([payment - (payment * ((inflation_rate/12)*i)) for i in range(loan_term - final_payment_time)])
