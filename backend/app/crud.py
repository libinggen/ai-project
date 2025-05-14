from sqlmodel import Session
from .models import Item

def create_item(session: Session, item: Item) -> Item:
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

def get_items(session: Session):
    return session.query(Item).all()
