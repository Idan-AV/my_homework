class RavKav:
    def __init__(self, holder_id: int, holder_name: str, balance: float, rides_log: str):
        self._rides_log = rides_log
        self._balance = balance
        self._holder_name = holder_name
        self._holder_id = holder_id
    
