from models.transaction import Transaction
from utils.decorators import validate_transaction
from utils.exceptions import InsufficientFundsError, NegativeAmountError

class Account: 
    bank_name = "BujaBank"
    
    # 문제2-1. 생성자 구현
    def __init__(self) -> None: 
        self.__balance = 0
        self.transactions = []
        
    # 문제2-2. 입금 메서드 구현
    @validate_transaction
    def deposit(self, amount: int) -> None: 
        # 예외처리
        if amount <= 0: 
            raise NegativeAmountError()
        
        self.__balance += amount
        self.transactions.append(Transaction("입금", amount, self.__balance))
    
    # 문제2-3. 출금 메서드 구현
    @validate_transaction
    def withdraw(self, amount: int) -> None: 
        # 예외처리
        if amount  <= 0: 
            raise NegativeAmountError()
        if amount > self.__balance: 
            raise InsufficientFundsError(self.__balance)
        
        self.__balance -= amount
        self.transactions.append(Transaction("출금", amount, self.__balance))
        
    # 문제2-4. 잔고 반환 메서드 구현
    def get_balance(self) -> int: 
        return self.__balance
    
    # 문제2-5. 거래 내역 반환 메서드 구현
    def get_transactions(self) -> list: 
        return self.transactions
    
    # 문제2-6. 클래스 변수 및 메서드 구현
    # 은행 이름 반환
    @classmethod
    def get_bank_name(cls) -> str: 
        return cls.bank_name
    
    # 은행 이름 설정
    @classmethod
    def set_bank_name(cls, name: str) -> None: 
        cls.bank_name = name
