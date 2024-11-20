from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from src.project.schemas.plane import PlaneSchema
from src.project.infrastructure.postgres.models import Plane
from src.project.core.config import settings

class PlaneRepository:
    _collection: Type[Plane] = Plane
    async def check_connection(
        self,
        session: AsyncSession,
    ) -> bool:
        query = "select 1;"
        result = await session.scalar(text(query))
        return True if result else False
    async def get_all_planes(
        self,
        session: AsyncSession,
    ) -> list[PlaneSchema]:
        query = f"select * from {settings.POSTGRES_SCHEMA}.planes;"
        planes = await session.execute(text(query))
        return [PlaneSchema.model_validate(obj=planes) for planes in planes.mappings().all()]