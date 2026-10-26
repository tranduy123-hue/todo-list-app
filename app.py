# Danh sách để lưu các công việc (mỗi công việc là một dictionary)
tasks = []


def add_task(task_name):
    """Thêm một công việc mới vào danh sách dạng dictionary."""
    task = {"name": task_name, "completed": False}
    tasks.append(task)
    print(f"Đã thêm công việc: '{task_name}'")


def complete_task(task_index):
    """Đánh dấu một công việc là hoàn thành dựa trên chỉ số (1-based)."""
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        print(f"Đã hoàn thành công việc: '{tasks[task_index - 1]['name']}'")
    else:
        print(f"Chỉ số công việc {task_index} không hợp lệ!")


def list_tasks():
    """Hiển thị tất cả công việc cùng trạng thái hoàn thành."""
    if not tasks:
        print("Danh sách công việc trống.")
        return
    print("\nDanh sách công việc:")
    for i, task in enumerate(tasks, start=1):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{i}. {status} {task['name']}")


# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    list_tasks()

    print("\nĐánh dấu hoàn thành công việc số 1:")
    complete_task(1)
    list_tasks()
