from ..models.user import UserSchema, UserDB
from ..db import database, users


#
# CREATES A NEW USER
# 

async def createUser(user: UserSchema):
    query = users.insert().values(
    		user_name = user.userName, 
    		first_name = user.firstName,
    		last_name = user.lastName)
    return await database.execute(query=query)

#
# GET ALL USERS
# 

async def getAllUsers():
    query = users.select()
    return await database.fetch_all(query=query)	