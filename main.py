from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Person(BaseModel):
    name: str
    age: int



@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Hello DevLaunch! From app1!"}


@app.get("/greet/{person_name}")
def greet_person(person_name: str) -> dict[str, str]:
    return {"greeting": f"Hello, {person_name}!"}


@app.post("/person/", status_code=201)
def create_person(person: Person) -> Person:
    print(f"Person {person.name} aged {person.age} created successfully.")
    return person


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
