from fastapi import APIRouter
from src.project.infrastructure.postgres.repository.plane_repo import PlaneRepository
from src.project.infrastructure.postgres.database import PostgresDatabase
from src.project.schemas.plane import PlaneSchema

router = APIRouter()

@router.get("/all_users", response_model=list[PlaneSchema])
async def get_all_users() -> list[PlaneSchema]:
    user_repo = PlaneRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        await user_repo.check_connection(session=session)
        all_users = await user_repo.get_all_planes(session=session)
    return all_users