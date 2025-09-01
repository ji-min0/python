from banking_system.models.user import User
from banking_system.utils.exceptions import UserNotFoundError

class BankingService: 
    # 문제4-1. 생성자 구현
    def __init__(self) -> None: 
        self.users = []
        
    # 문제4-2. 사용자 추가 메서드 구현
    def add_user(self, username: str) -> None: 
        self.users.append(User(username))
        
    # 문제4-3. 사용자 찾기 메서드 구현
    def find_user(self, username: str) -> User: 
        for user in self.users: 
            if user.username == username: 
                return user
        raise UserNotFoundError(username)
    
    # 문제4-4. 사용자 메뉴 제공 메서드 구현
    def user_menu(self, username: str) -> None: 
        # 사용자 찾기
        user = self.find_user(username)
        # 입금, 출금, 잔고확인, 거래내역 기능 반복루프
        while True: 
            try: 
                choice = input("원하는 메뉴를 선택하세요 (1: 입금, 2: 출금, 3: 잔고확인, 4: 거래 내역, 0: 종료)")
                if choice == "1": 
                    amount = int(input("입금할 금액을 입력하세요: "))
                    user.account.deposit(amount)
                elif choice == "2": 
                    amount = int(input("출금할 금액을 입력하세요: "))
                    user.account.withdraw(amount)
                elif choice == "3": 
                    print(f"현재 잔액은 {user.account.get_balance()}원 입니다.")
                elif choice == "4": 
                    for transaction in user.account.get_transactions(): 
                        print(transaction)
                elif choice == "0": 
                    break
                else: 
                    print("잘못된 입력입니다. 다시 시도하세요.")
            
            except ValueError as e: 
                print(f"잘못된 입력입니다: {e}")
            except InsufficientFundsError as e: 
                print(f"⛔️ 잔고 부족: {e}")
            except NegativeamountError as e: 
                print(f"⛔️ 입력 금액 오류: {e}")
            except UserNotFoundError as e: 
                print(f"⛔️ 사용자 오류: {e}")