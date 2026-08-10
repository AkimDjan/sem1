from uuid import UUID
from metrics import PeriodActiveUsers
st=set()

users=[
        UUID("2509a9eb-2422-4b83-8911-f780eea815bb"),
        UUID("f52fc9b2-2ff2-4419-9f07-22267946b46e"),
    ]

for user in users:
    st.add(user)

print(len(st))
