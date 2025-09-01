from banking_system.models.account import Account

class User: 
    # 문제3-1. 생성자 구현
    def __init__(self, username: str) -> None: 
        self.username = username
        self.account = Account()