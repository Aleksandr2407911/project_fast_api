
from fastapi import FastAPI

from contextlib import asynccontextmanager

from database import delete_tables, create_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")
    # Clean up the ML models and release the resources

app = FastAPI(lifespan = lifespan)
app.include_router(tasks_router)

