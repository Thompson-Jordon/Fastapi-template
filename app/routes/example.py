from fastapi import APIRouter, Depends, HTTPException
from typing import List, Any
from sqlalchemy.orm import Session
from app.dependencies import get_db

from app.schemas import schemas
from app.actions import actions
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from pydantic import UUID4


router = APIRouter(tags=["posts"])


@router.get("/")
def index():
    return {"message": "Hello world!"}


@router.get("/posts", response_model=List[schemas.Post])
def list_posts(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    posts = actions.post.get_all(db=db, skip=skip, limit=limit)
    return posts


@router.post(
    "/posts", response_model=schemas.Post, status_code=HTTP_201_CREATED
)
def create_post(*, db: Session = Depends(get_db), post_in: schemas.PostCreate) -> Any:
    post = actions.post.create(db=db, obj_in=post_in)
    return post


@router.put(
    "/posts/{id}",
    response_model=schemas.Post,
)
def update_post(
    *,
    db: Session = Depends(get_db),
    id: UUID4,
    post_in: schemas.PostUpdate,
) -> Any:
    post = actions.post.get(db=db, id=id)
    if not post:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Post not found")
    post = actions.post.update(db=db, db_obj=post, obj_in=post_in)
    return post


@router.get(
    "/posts/{id}",
    response_model=schemas.Post,
)
def get_post(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    post = actions.post.get(db=db, id=id)
    if not post:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Post not found")
    return post


@router.delete(
    "/posts/{id}",
    response_model=schemas.Post,
)
def delete_post(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    post = actions.post.get(db=db, id=id)
    if not post:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Post not found")
    post = actions.post.remove(db=db, id=id)
    return post
