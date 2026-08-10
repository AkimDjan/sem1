from uuid import UUID
from metrics import PeriodActiveUsers


pau = PeriodActiveUsers(accumulation_period=3)
pau.add_active_users_for_curr_day(
    [
        UUID("52d6f353-4dd3-421b-b1c4-c35d2ae9ad66"),
        UUID("3f06aef7-bf3a-41f8-b571-3453a3b27aa9"),
        UUID("b6595baa-a23a-4e22-8656-079f84c7c3a4"),
        UUID("52d6f353-4dd3-421b-b1c4-c35d2ae9ad66"),
        UUID("52d6f353-4dd3-421b-b1c4-c35d2ae9ad66"),
        UUID("b6595baa-a23a-4e22-8656-079f84c7c3a4"),
    ],
)
assert pau.unique_users_amount == 3