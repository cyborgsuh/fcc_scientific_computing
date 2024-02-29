import math
class Category:
    def __init__(self,category) -> None:
        self.category=category 
        self.ledger=[]
    def deposit(self,amount,description=''):
        self.ledger.append({"amount":amount,"description":description})
    def withdraw(self,amount,description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount":-amount,"description":description})
            return True
        return False
    def get_balance(self):
        return sum(i['amount'] for i in self.ledger)
    def transfer(self,amount,category):
        if self.check_funds(amount):
            self.withdraw(amount,f'Transfer to {category.category}')
            category.deposit(amount,f'Transfer from {self.category}')
            return True
        return False
    def check_funds(self,amount):
        return (amount<=self.get_balance())
            
    def __str__(self) -> str:
        title=f'{self.category:*^30}\n'
        items=''
        total=0
        for i in self.ledger:
            items+=f"{i['description'][0:23]:23}"+f"{i['amount']:7.2f}"+"\n"
            total+=i['amount']
        format(total,".2f")
        total=str(total)
        output=title+items+f"Total: {total}"
        return output


def create_spend_chart(categories):
    totals = {}
    total = 0
    chart = "Percentage spent by category\n"
    for category in categories:
        totals[category.category] = 0
        for entry in category.ledger:
            if entry["amount"] < 0:
                totals[category.category] = totals[category.category] + entry["amount"]

    for k, v in totals.items():
        totals[k] = v * - 1
        total = total - v

    for k, v in totals.items():
        percentage = math.trunc((v / total * 100))
        totals[k] = percentage


    for i in range(100, -10, -10):
        chart = chart + str(i).rjust(3, " ") + "|"
        for k, v in totals.items():
            if v >= i:
                chart = chart + " o "
            else:
                chart = chart + "   "
        chart = chart + " \n"

    chart = chart + 4 * " " + (4 + 2 * len(totals)) * "-"
    i = 0
    while i < max(len(k) for k, v in totals.items()):
        chart = chart + "\n" + 4 * " "
        for key in totals:
            if len(key) <= i:
                chart = chart + "   "
            else:
                chart = chart + " " + key[i] + " "
        chart = chart + " "
        i = i + 1

    return chart
        
        
food=Category("Food")
entertainment=Category("Entertainment")
business=Category("Business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([business, food, entertainment]))