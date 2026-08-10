from uuid import UUID
from metrics import PeriodActiveUsers


pau = PeriodActiveUsers(accumulation_period=1)
pau.add_active_users_for_curr_day(
    [
        UUID("2509a9eb-2422-4b83-8911-f780eea815bb"),
        UUID("f52fc9b2-2ff2-4419-9f07-22267946b46e"),
    ],
)
assert pau.unique_users_amount == 2