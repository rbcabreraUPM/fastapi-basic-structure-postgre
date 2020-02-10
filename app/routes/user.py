from fastapi import APIRouter
from typing import List
from starlette.responses import JSONResponse
from starlette.status import *

# import user model and services
from ..models.user import UserSchema, UserDB, UserResponseSchema
from ..services import user as userService

router = APIRouter()

# POST 
# Creates a new User
@router.post("/createUser")
async def createUser(user: UserSchema):
	user_primary_key = await userService.createUser(user)
	user_response = {
        "id": user_primary_key,
        "userName": user.userName,
       	"firstName": user.firstName,
       	"lastName": user.lastName
    }
	return JSONResponse(status_code=HTTP_201_CREATED, content=user_response)

@router.get("/getAllUsers", response_model=List[UserResponseSchema])
async def getAllUsers():
    return await userService.getAllUsers()
