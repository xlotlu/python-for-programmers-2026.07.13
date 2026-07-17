# date fiind "data/clients.json" și "data/transactions.csv"

# creați clasele
# Client și BankAccount


# Client:
#  - name
#  - email
#  - accounts: []

# BankAccount:
#  - id
#  - overdraft
#  - amount


import json
import csv

class BankAccount:
    ALL_ACCOUNTS = {}

    def __init__(self, id, overdraft=0):
        self.id = id
        self.overdraft = overdraft
        self.amount = 0

        # don't forget to cache myself
        self.ALL_ACCOUNTS[id] = self

    def __repr__(self):
        return f"{self.__class__.__name__}" \
               f"({repr(self.id)}, overdraft={repr(self.overdraft)})"

    def credit(self, amount):
        self.amount += amount

    def debit(self, amount):
        available_amount = self.amount + self.overdraft
        if amount <= available_amount:
            self.amount -= amount
        else:
            raise ValueError("Insufficient funds")

    @classmethod
    def get_by_id(cls, id):
        return cls.ALL_ACCOUNTS[id]


class Client:
    def __init__(self, name, email, accounts=None):
        self.name = name
        self.email = email
        self.accounts = [] if accounts is None else accounts

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"(name={repr(self.name)}, email={repr(self.email)}, accounts={repr(self.accounts)})"
        )

    @classmethod # useful for factory methods
    def from_dictionary(cls, d):
        return cls(d["name"], d["email_address"], accounts=[
            BankAccount(**acc)
            for acc in d["bank_accounts"]
        ])


if __name__ == '__main__':
    # do the import
    with open("data/clients.json") as f:
        for cldict in json.load(f):
            c = Client.from_dictionary(cldict)
            print(c)

    with open("data/transactions.csv") as f:
        for t in csv.DictReader(f):
            id = int(t['account_id'])
            # problem:
            # we need to retrieve the account with this `id`
            # to operate on it

            account = BankAccount.get_by_id(id)

            type = t['transaction_type']
            amount = float(t['amount'])

            if type == "credit":
                account.credit(amount)
            elif type == "debit":
                account.debit(amount)
            else:
                # this is a bug in the dataset
                print('error!')
                # we should probably rollback everything

    for id, acc in BankAccount.ALL_ACCOUNTS.items():
        print(id, acc.amount)
