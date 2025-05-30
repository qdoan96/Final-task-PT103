# Final-task-PT103
This is the final task of PT103 class
# To-Do App - Quản lý danh sách công việc với FastAPI

## Mô tả dự án

Đây là một RESTful API cho phép quản lý danh sách công việc (To-Do List) sử dụng **FastAPI**. API hỗ trợ các chức năng cơ bản như:

- Tạo công việc mới
- Xem danh sách công việc (có lọc, sắp xếp, phân trang)
- Xem chi tiết công việc
- Cập nhật công việc
- Xóa công việc

Dữ liệu được lưu trữ tạm thời trong bộ nhớ (in-memory list).

---

## Yêu cầu kỹ thuật

- Python 3.8+
- FastAPI
- Uvicorn
- Pydantic

---

## Cài đặt

1. **Clone project về máy:**
   ```bash
   git clone <link-github-cua-ban>
   cd <ten-thu-muc-project>

2. Cài đặt thư viện cần thiết:
pip install fastapi uvicorn

---

## Cách chạy ứng dụng

1. Chạy server FastAPI:
uvicorn Baithicuoikhoa:app --reload
Note: Baithicuoikhoa là tên file Python chứa mã nguồn API (bỏ đuôi .py); app là tên biến FastAPI trong file.

2.Truy cập tài liệu API (Swagger UI):
Mở trình duyệt và vào địa chỉ: http://127.0.0.1:8000/docs
Tại đây bạn có thể thử tất cả các endpoint, nhập dữ liệu JSON và xem kết quả trực tiếp.

---
### Ví dụ các endpoint
Tạo công việc mới:
POST /tasks/
{
  "title": "Learn FastAPI",
  "description": "Build an API using FastAPI",
  "priority": 1
}

Xem danh sách công việc:
GET /tasks/

Xem chi tiết công việc:
GET /tasks/{task_id}

Cập nhật công việc:
PUT /tasks/{task_id}

Xóa công việc:
DELETE /tasks/{task_id}
