from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from auth.base_config import current_user
from auth.models import User
from tasks.models import Task
from database import get_async_session
from tasks.schemas import TaskCreate, TaskUpdate

from fastapi_cache.decorator import cache

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get('/')
@cache(expire=60)
async def get_tasks(session: AsyncSession = Depends(get_async_session),
                    user: User = Depends(current_user)):
    query = select(Task)
    result = await session.execute(query)
    return result.mappings().all()


@router.get('/{task_id}')
@cache(expire=60)
async def get_task(task_id: int,
                   session: AsyncSession = Depends(get_async_session),
                   user: User = Depends(current_user)):
    query = select(Task).where(Task.id == task_id)
    result = await session.execute(query)
    return result.mappings().all()


@router.post('/')
async def create_task(new_task: TaskCreate,
                      session: AsyncSession = Depends(get_async_session),
                      user: User = Depends(current_user)):
    query = insert(Task).values(title=new_task.title,
                                description=new_task.description,
                                user_id=user.id)
    await session.execute(query)
    await session.commit()
    return new_task


@router.put('/{task_id}')
async def update_task(task_id: int, modified_task: TaskUpdate,
                      session: AsyncSession = Depends(get_async_session),
                      user: User = Depends(current_user)):
    try:
        query = select(Task).where(Task.id == task_id)
        result = await session.execute(query)
        task = result.scalar_one()
        if task.user_id != user.id:
            return "Нельзя изменить задачу другого пользователя"
        task.title = modified_task.title
        task.description = modified_task.description
        await session.commit()
        return f"Задача {task_id} изменена"
    except NoResultFound:
        return "Нет такой задачи или она была удалена"


@router.delete("/{task_id}")
async def delete_task(task_id: int,
                      session: AsyncSession = Depends(get_async_session),
                      user: User = Depends(current_user)):
    try:
        query = select(Task).where(Task.id == task_id)
        result = await session.execute(query)
        task = result.scalar_one()
        if task.user_id != user.id:
            return "Нельзя удалить задачу другого пользователя"
        await session.delete(task)
        await session.commit()
        return f"Задача {task_id} удалена"
    except NoResultFound:
        return "Нет такой задачи или она уже была удалена"
