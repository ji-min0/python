# 잔고 부족 예외 클래스
class InsufficientFundsError(Exception): 
    def __init__(self, balance: int) -> None: 
        super.__init__(f"잔액이 부족합니다. 현재 잔액: {balance}원")

# 음수 금액 입력 예외 클래스
class NegativeAmountError(Exception): 
    def __init__(self) -> None: 
        super.__init__("음수는 허용되지 않습니다.")

# 사용자 찾기 실패 예외 클래스
class UserNotFoundError(Exception): 
    def __init__(self, username: str) -> None: 
        super().__init__(f"사용자를 찾을 수 없습니다: {username}")
