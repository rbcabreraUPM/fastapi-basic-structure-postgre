from fastapi import APIRouter, Path,HTTPException
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
    if isinstance(user_primary_key, dict):
        print(user_primary_key)
        raise HTTPException(status_code=user_primary_key['status_code'], detail= user_primary_key['description'])
    user_response = {
        "id": user_primary_key,
        "userName": user.userName,
       	"firstName": user.firstName,
       	"lastName": user.lastName
    }
    return JSONResponse(status_code=HTTP_201_CREATED, content=user_response)


# GET 
# RETURNS ALL DATA AS A LIST OF DICTIONARIES(JSON)
@router.get("/getAllUsers", response_model=List[UserResponseSchema])
async def getAllUsers():
    return await userService.getAllUsers()

# GET ALL USERS
# RETURNS ALL DETAILS
@router.get("/{id}/", response_model=UserResponseSchema)
async def getUser(id: int = Path(..., gt=0),):
    user = await userService.getUser(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/updateUser/{id}/",response_model=UserResponseSchema)
async def updateUser(user: UserSchema, id: int = Path(..., gt=0),):
    userExist = await userService.getUser(id)
    if not userExist:
        raise HTTPException(status_code=404, detail="User not found")

    updatedUser = await userService.updateUser(id, user)
    return updatedUser


@router.delete("/deleteUser/{id}/", response_model=UserResponseSchema)
async def deleteUser(id: int = Path(..., gt=0)):
    userExist = await userService.getUser(id)
    if not userExist:
        raise HTTPException(status_code=404, detail="User not found")

    await userService.deleteUser(id)
    return userExist
