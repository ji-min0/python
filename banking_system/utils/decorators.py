from typing import Callable

def validate_transaction(func: Callable) -> Callable:
    # 문제5-1. 데코레이터 구현
    def wrapper(self, amount: int) -> None:
        if amount <= 0: 
            raise ValueError("금액은 0보다 커야합니다.")
        return func(self, amount)
    return wrapper
