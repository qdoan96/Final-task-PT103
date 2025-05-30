"""Bài tập cuối khoá
Hạn nộp: 15/6
# Quản lý danh sách công việc (To-Do App)
Xây dựng một RESTful API với các chức năng sau:

1. Tạo công việc mới

- Endpoint: POST /tasks/

- Input:

```
{
  "title": "Learn FastAPI",
  "description": "Build an API using FastAPI",
  "priority": 1
}

```

- Output: task vừa tạo với id, status = "pending", created_at

2. Xem danh sách công việc

- Endpoint: GET /tasks/

- Tùy chọn: lọc theo status (pending, done), sắp xếp theo priority, phân trang (limit, offset)

3. Xem chi tiết công việc

- Endpoint: GET /tasks/{task_id}

- Trả về thông tin chi tiết của task

4. Cập nhật công việc

- Endpoint: PUT /tasks/{task_id}

- Cho phép cập nhật title, description, priority, status

5. Xóa công việc

- Endpoint: DELETE /tasks/{task_id}

- Trả về "message": "Task deleted successfully"


## Yêu cầu kỹ thuật

- Sử dụng FastAPI (https://fastapi.tiangolo.com/)

- Dữ liệu lưu trong JSON file hoặc in-memory list

- Sử dụng pydantic để validate input

- Ghi chú rõ các phần logic chính bằng comment

## Hướng dẫn nộp bài

- Gửi link GitHub project

- Kèm theo ảnh chụp Swagger UI hoặc curl test

- Có file README.md mô tả project + cách chạy"""


from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

app = FastAPI()

# In-memory data store
tasks = [
    {"id": 1, "title": "Học Python", "description": "Học cú pháp cơ bản", "priority": 1},
    {"id": 2, "title": "Học FastAPI", "description": "Tạo REST API đơn giản", "priority": 3},
    {"id": 3, "title": "Viết bài tập cuối khóa", "description": "Xây dựng ứng dụng thực tế", "priority": 2},
]
task_id_counter = 1

# Pydantic models
class TaskCreate(BaseModel):
    title: str
    description: str
    priority: int = 1

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[int] = None
    status: Optional[str] = None

class Task(BaseModel):
    id: int
    title: str
    description: str
    priority: int
    status: str
    created_at: datetime

# Helper function to get next id
def get_next_id():
    global task_id_counter
    task_id = task_id_counter
    task_id_counter += 1
    return task_id

# 1. Tạo công việc mới
@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    new_task = Task(
        id=get_next_id(),
        title=task.title,
        description=task.description,
        priority=task.priority,
        status="pending",
        created_at=datetime.now()
    )
    tasks.append(new_task)
    return new_task

# 2. Xem danh sách công việc (lọc, sắp xếp, phân trang)
@app.get("/tasks/", response_model=List[Task])
def list_tasks(
    status: Optional[str] = Query(None, description="Lọc theo trạng thái"),
    sort_by_priority: Optional[bool] = Query(False, description="Sắp xếp theo priority"),
    limit: Optional[int] = Query(None, description="Giới hạn số lượng"),
    offset: Optional[int] = Query(0, description="Bắt đầu từ vị trí")
):
    filtered = tasks
    if status:
        filtered = [t for t in filtered if t.status == status]
    if sort_by_priority:
        filtered = sorted(filtered, key=lambda x: x.priority)
    if limit is not None:
        filtered = filtered[offset:offset+limit]
    else:
        filtered = filtered[offset:]
    return filtered

# 3. Xem chi tiết công việc
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# 4. Cập nhật công việc
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: TaskUpdate):
    for task in tasks:
        if task.id == task_id:
            if task_update.title is not None:
                task.title = task_update.title
            if task_update.description is not None:
                task.description = task_update.description
            if task_update.priority is not None:
                task.priority = task_update.priority
            if task_update.status is not None:
                task.status = task_update.status
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# 5. Xóa công việc
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(i)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")

