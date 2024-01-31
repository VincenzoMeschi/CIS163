from typing import List

class Customer:

    def __init__(self, id: int, name: str, balance_owed: float, transactions: list[float]):
        self.__id = id
        self.__name = name
        self.__balance_owed = balance_owed
        self.__transactions = transactions

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id
    
    def get_transactions(self):
        return self.__transactions
    
    def get_balance(self):
        self.reconcile()
        return self.__balance_owed
    
    def set_name(self, new_name: str):
        try:
          if isinstance(new_name, str):
            self.__name = new_name
          else:
              raise ValueError()
        except:
            return "Invalid name!"

    def set_id(self, new_id: int):
        try:
            if isinstance(new_id, int):
                self.__id = new_id
            else:
                raise ValueError()
        except:
                return "Invalid id!"
    
    def set_transactions(self, transactions: List[float | int]):
        try:
            
            if isinstance(transactions, list):
              for _ in transactions:
                  if not isinstance(_, (float, int)):
                      raise ValueError()
              self.__transactions = transactions
            else:
                raise ValueError()
        except:
            return "Invalid id!"
        
    
    def reconcile(self):
        total = sum(self.get_transactions())
        if total < 0:
            if isinstance(self, VIP):
                print(f"{self.get_title()} {self.get_name()}, would you please remit payment at your earliest convenience.")
            else:
                print(f"{self.get_name()}, pay your balance immediately!")
        
        self.__balance_owed = total

class VIP(Customer):
    
    def __init__(self, id: int, name: str, balance_owed: float, transactions: List[float], title: str):
        super().__init__(id=id, name=name, balance_owed=balance_owed, transactions=transactions)
        self.__title = title
    
    def get_title(self):
        return self.__title
    
    def set_title(self, title):
        titles = ("Mr.", "Ms.", "Dr.")
        try:
          if isinstance(title, str) and title in titles:
              self.__title = title
          else:
              raise ValueError()
        except:
            return "Invalid title!" 