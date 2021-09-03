from app.schemas.user import UserSignIn
from app import crud
from fastapi import APIRouter
from app.core.authen_handler import auth_handler
from fastapi.exceptions import HTTPException
from fastapi import status

router = APIRouter()


@router.post("/sign_in")
def sign_in(data: UserSignIn):
    user = crud.user.get_by_username(data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    verified_user = auth_handler.verify_password(data.password, user.hashed_password)
    if not verified_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return {
        "access_token": auth_handler.encode_token(user.username),
        "refresh_token": auth_handler.encode_refresh_token(user.username),
    }


@router.post("/sign_up")
def sign_up(data: UserSignIn):
    user = crud.user.get_by_username(data.username)
    if user:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Username is already existed",
        )
    new_user = crud.user.create(data)
    return {"message": f"{new_user.username} created sucessfully"}
