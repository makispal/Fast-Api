from fastapi import status, Depends, APIRouter
from fastapi.exceptions import HTTPException
from ..database import get_db
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from typing import List


router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.get("/", response_model=List[schemas.UserOut])
def get_posts(db: Session = Depends(get_db)) -> List:
    users = db.query(models.User).all()
    return users


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)) -> dict:
    hashed_password = utils.to_hash(user.password)
    user.password = hashed_password    
    new_user = models.User(**user.dict())
    print(hashed_password)
    print(user.password)
    print(new_user)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)) -> dict:
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"User With ID:{id} does not exists!!")    
    return user