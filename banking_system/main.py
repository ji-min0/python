from services.banking_services import BankingService
from utils.exceptions import InsufficientFundsError, NegativeAmountError, UserNotFoundError

def main() -> None: 
    system = BankingService()
    
    while True: 
        try: 
            choice = input("1: 사용자 추가, 2: 사용자 찾기, 0: 종료 : ")
            if choice == "1": 
                username = input("사용자 이름을 입력하세요: ")
                system.add_user(username)
                
            elif choice == "2": 
                username = input("사용자 이름을 입력하세요: ")
                system.user_menu(username)
                
            elif choice == "0": 
                break
            else: 
                print("잘못된 입력입니다. 다시 시도하세요.")
        
        except ValueError as e: 
            print(f"잘못된 입력입니다: {e}")
        except InsufficientFundsError as e: 
            print(f"⛔️ 잔고 부족: {e}")
        except NegativeAmountError as e: 
            print(f"⛔️ 입력 금액 오류: {e}")
        except UserNotFoundError as e: 
            print(f"⛔️ 사용자 오류: {e}")
            
if __name__ == "__main__":
    main()