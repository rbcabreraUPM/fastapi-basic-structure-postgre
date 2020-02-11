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


async def getUser(id: int):
    query = users.select().where(id == users.c.id)
    return await database.fetch_one(query=query)

async def updateUser(id: int, user: UserSchema):
    query = (
        users
        .update()
        .where(id == users.c.id)
        .values(first_name=user.firstName, last_name=user.lastName)
        .returning(users.c.id, users.c.first_name, users.c.last_name,users.c.user_name)
    )
    return await database.fetch_one(query=query)


async def deleteUser(id: int):
    query = users.delete().where(id == users.c.id)
    return await database.execute(query=query)
