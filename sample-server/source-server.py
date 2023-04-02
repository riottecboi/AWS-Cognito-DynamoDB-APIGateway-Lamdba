import uvicorn
import random
from faker import Faker
from fastapi import Depends, FastAPI

fake = Faker()
app = FastAPI()

def random_user_records():
    records = []
    # random number of looping & fake generated records
    for _ in range(random.randint(0,10)):
        records.append(fake.profile())
    return records
@app.get("/")
async def read_current_user(records: list = Depends(random_user_records)):
    return records

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
