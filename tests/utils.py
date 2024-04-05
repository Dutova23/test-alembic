from httpx import AsyncClient

async def create_user(client: AsyncClient, user):
    response = await client.post("/api/users", json = user)
    user_id = response.json()["user_id"]
    return user_id

