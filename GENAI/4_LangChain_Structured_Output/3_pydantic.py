from pydantic import BaseModel
from typing import Optional

# Define schema using Pydantic
class Student(BaseModel):
    name: str   # <-- expects a string
    age:Optional[int] = None

# Input dict with correct type (string)
new_student = {"name": "karthik","age":'32'}

# Input dict with incorrect type (int instead of str)
new_diff_student = {"name": 88}

# ✅ This works, because "karthik" is already a string
student = Student(**new_student)

# ❌ This raises ValidationError, because "88" is not str
# (Pydantic will try to coerce it, but str is strict in this case)
diff_student = Student(**new_diff_student)

print(student)       # Student(name='karthik')
# print(diff_student) # Uncomment → will throw ValidationError
