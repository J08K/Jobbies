import redis
import datetime

class JobbiesDB:
    conn: redis.Connection
    
    def __init__(self) -> None:
        self.conn = redis.Redis(host="localhost", port=6379, decode_responses=True)
        
        if self.conn.get(self.cur_target) is None:
            print("Creating new entry...")
            self.conn.set(self.cur_target, 0)

    @property
    def cur_target(self) -> str:
        today = datetime.datetime.today()
        return f"count:{today.year}:{today.month}"

    def get_count(self) -> int:
        result = self.conn.get(self.cur_target)
        
        if result is None:
            self.conn.set(self.cur_target, 0)
            return 0

        return int(self.conn.get(self.cur_target))

    def add_one(self) -> int:
        cur_count = self.get_count()
        
        self.conn.set(self.cur_target, cur_count + 1)
        
        return cur_count + 1