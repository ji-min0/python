class Transaction: 
    
    # 문제1-1. 생성자 구현
    def __init__(self, transaction_type: str, amount: int, balance: int) -> None: 
        self.transaction_tpye = transaction_type
        self.amount = amount
        self.balance = balance
    
    # 문제1-2. 문자열 반환 메서드 구현
    def __str__(self) -> str: 
        return f"{self.transaction_tpyen}: {self.amount}원, 잔액: {self.balance}원"
    
    # 문제1-3. 튜플 반환 메서드 구현
    def to_tuple(self) -> tuple: 
        return self.transaction_tpye, self.amount, self.balance
    