import os
import shutil
import tkinter as tk
from tkinter import messagebox

paths_to_check = [
    r"C:\ProgramData",
    os.environ["LOCALAPPDATA"],
    os.environ["APPDATA"]
]

def find_folders():
    found = []
    for base in paths_to_check:
        for root, dirs, files in os.walk(base):
            for d in dirs:
                if "capcut" in d.lower() or "bytedance" in d.lower():
                    found.append(os.path.join(root, d))
    return found

def on_find():
    global found_folders
    found_folders = find_folders()
    if found_folders:
        msg = "Найдены папки:\n" + "\n".join(found_folders)
    else:
        msg = "Следов CapCut / Bytedance не найдено."
    messagebox.showinfo("Результат поиска", msg)

def on_delete():
    if not found_folders:
        messagebox.showinfo("Удаление", "Нет папок для удаления.")
        return
    confirm = messagebox.askyesno("Подтверждение", "Удалить найденные папки?")
    if confirm:
        for folder in found_folders:
            try:
                shutil.rmtree(folder)
            except Exception as e:
                messagebox.showwarning("Ошибка", f"Не удалось удалить: {folder}\n{e}")
        messagebox.showinfo("Готово", "Удаление завершено.")

app = tk.Tk()
app.title("CapCut Cleaner")
app.geometry("400x200")

tk.Button(app, text="Найти следы", command=on_find).pack(pady=10)
tk.Button(app, text="Удалить найденное", command=on_delete).pack(pady=10)
tk.Button(app, text="Закрыть", command=app.quit).pack(pady=10)

found_folders = []
app.mainloop()
