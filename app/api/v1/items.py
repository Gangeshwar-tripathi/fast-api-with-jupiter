from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.responses import HTMLResponse


router = APIRouter()


class Item(BaseModel):
    id: int
    name: str
    description: str | None = None


# In-memory store for example. Replace with DB access.
ITEMS =ITEMS = {
    1: {
        "id": 1,
        "name": f"Item 1",
        "description": f"Description for item 1"
    }

}

@router.get("/", response_model=List[Item])
async def list_items():
    return list(ITEMS.values())


@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int):
    item = ITEMS.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/", response_model=Item, status_code=201)
async def create_item(item: Item):
    if item.id in ITEMS:
        raise HTTPException(status_code=400, detail="ID exists")
    ITEMS[item.id] = item.dict()
    return item