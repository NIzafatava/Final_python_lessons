# Написать класс банковский аккаунт. Хранить баланс, и историю операций над аккаунтом.
# Добавить методы пополнения баланса и снятия средств с баланса. Класс для истории должен
# хранить операцию (снятие или пополнение), сумму, дату и время операции.
# Создать экземпляр банковского аккаунта и проверить его работу.

from datetime import datetime


# class BankAccount:   - не используется
#     def __init__(self, account_balance: int):
#         self.account_balance = account_balance

class BankAccountHistory:

    def __init__(self, account_balance: int):
        self.account_balance = account_balance
        self.add_history = []
        self.withdraw_history = []
        self.add_history_time = []
        self.withdraw_history_time = []

    def add_balance(self, sum_to_add: int):
        self.account_balance += sum_to_add
        call_date_time_unformatted = datetime.now()
        call_date = call_date_time_unformatted.strftime("%d/%m/%y %I:%M")
        self.add_history_time.append(call_date)
        self.add_history.append(sum_to_add)
        print(f'операция пополнения {self.account_balance}')

    def withdraw_balance(self, sum_to_withdraw: int):
        if sum_to_withdraw <= self.account_balance:
            self.account_balance -= sum_to_withdraw
            call_date_time_unformatted = datetime.now()
            call_date = call_date_time_unformatted.strftime("%d/%m/%y %I:%M")
            self.withdraw_history_time.append(call_date)
            self.withdraw_history.append(sum_to_withdraw)
            print(f'операция снятия {self.account_balance}')
        else:
            print('Недотаточно средств для снятия')

    def transaction_history(self):
        result_for_add = tuple(zip(self.add_history, self.add_history_time))
        result_for_withdraw = tuple(zip(self.add_history, self.add_history_time))
        print(f'операции пополнения счета: {result_for_add}')
        print(f'операции снятия со счета : {result_for_withdraw}')


my_account = BankAccountHistory(100)
my_account.add_balance(10)
my_account.withdraw_balance(20)
my_account.add_balance(30)
my_account.transaction_history()



"""output:
операция пополнения 110
операция снятия 90
операция пополнения 120
операции пополнения счета: ((10, '29/03/23 07:09'), (30, '29/03/23 07:09'))
операции снятия со счета : ((10, '29/03/23 07:09'), (30, '29/03/23 07:09'))"""

