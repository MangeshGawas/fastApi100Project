from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.todo_model import Todo
from app.models.user_model import User

from app.schemas.todo_schema import (
    TodoCreate
)

from app.utils.jwt_handler import (
    get_current_user
)

router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)


@router.post("/")
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    new_todo = Todo(
        title=todo.title,
        description=todo.description,
        owner_id=current_user.id
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo


@router.get("/")
def get_all_todos(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    todos = db.query(Todo).filter(
        Todo.owner_id == current_user.id
    ).all()

    return todos