from fastapi import FastAPI, Depends
from sqlmodel import Session
from contextlib import asynccontextmanager

from .models import Item
from .database import create_db_and_tables, get_session
from .crud import create_item, get_items

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup 初始化
    create_db_and_tables()
    yield
    # shutdown 清理（可选）

app = FastAPI(lifespan=lifespan)

@app.post("/items/", response_model=Item)
def create(item: Item, session: Session = Depends(get_session)):
    return create_item(session, item)

@app.get("/items/", response_model=list[Item])
def read_items(session: Session = Depends(get_session)):
    return get_items(session)
