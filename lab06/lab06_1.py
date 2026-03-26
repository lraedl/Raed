import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# Подключаем наш пакет particles (папка particles/__init__.py)
from particles import PARTICLES, udelny_zaryad, kompton, v_word, v_excel

# ─── Функция расчёта ────────────────────────────────────────────

def rasschitat():
    name = combo.get()           # берём выбранное имя из выпадающего списка

    mass   = PARTICLES[name]["mass"]    # масса частицы
    charge = PARTICLES[name]["charge"]  # заряд частицы

    # Считаем по формулам из модуля formuly.py
    spec = udelny_zaryad(charge, mass)
    komp = kompton(mass)

    # Показываем результаты в окне
    lbl_mass.config(   text=f"Масса:                    {mass:.3e} кг")
    lbl_charge.config( text=f"Заряд:                    {charge:.3e} Кл")
    lbl_spec.config(   text=f"Удельный заряд:           {spec:.3e} Кл/кг")
    lbl_compton.config(text=f"Комптоновская длина волны:{komp:.3e} м")

    # Запоминаем результат, чтобы потом можно было сохранить
    app.result = {"name": name, "mass": mass, "charge": charge,
                  "spec_charge": spec, "compton": komp}

# ─── Функции сохранения ─────────────────────────────────────────

def sohranit_word():
    if not hasattr(app, "result"):
        messagebox.showwarning("Нет данных", "Сначала нажмите Рассчитать!")
        return
    path = filedialog.asksaveasfilename(defaultextension=".docx",
                                        filetypes=[("Word", "*.docx")])
    if path:
        v_word([app.result], path)
        messagebox.showinfo("Готово", f"Сохранено: {path}")


def sohranit_excel():
    if not hasattr(app, "result"):
        messagebox.showwarning("Нет данных", "Сначала нажмите Рассчитать!")
        return
    path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                        filetypes=[("Excel", "*.xlsx")])
    if path:
        v_excel([app.result], path)
        messagebox.showinfo("Готово", f"Сохранено: {path}")


def sohranit_vse_word():
    # Считаем все три частицы и сохраняем в один файл
    results = []
    for name, data in PARTICLES.items():
        results.append({
            "name":        name,
            "mass":        data["mass"],
            "charge":      data["charge"],
            "spec_charge": udelny_zaryad(data["charge"], data["mass"]),
            "compton":     kompton(data["mass"]),
        })
    path = filedialog.asksaveasfilename(defaultextension=".docx",
                                        filetypes=[("Word", "*.docx")])
    if path:
        v_word(results, path)
        messagebox.showinfo("Готово", f"Сохранено: {path}")


def sohranit_vse_excel():
    results = []
    for name, data in PARTICLES.items():
        results.append({
            "name":        name,
            "mass":        data["mass"],
            "charge":      data["charge"],
            "spec_charge": udelny_zaryad(data["charge"], data["mass"]),
            "compton":     kompton(data["mass"]),
        })
    path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                        filetypes=[("Excel", "*.xlsx")])
    if path:
        v_excel(results, path)
        messagebox.showinfo("Готово", f"Сохранено: {path}")

# ─── Создание окна ──────────────────────────────────────────────

app = tk.Tk()
app.title("Элементарные частицы")
app.resizable(False, False)

FONT       = ("Segoe UI", 11)
FONT_BOLD  = ("Segoe UI", 11, "bold")
FONT_TITLE = ("Segoe UI", 14, "bold")
PAD = {"padx": 12, "pady": 6}

# Заголовок
tk.Label(app, text="Расчёт параметров элементарных частиц",
         font=FONT_TITLE).pack(**PAD)

# Разделитель
ttk.Separator(app, orient="horizontal").pack(fill="x", padx=12)

# Выбор частицы
frame_input = tk.Frame(app)
frame_input.pack(**PAD)

tk.Label(frame_input, text="Выберите частицу:", font=FONT).grid(row=0, column=0, sticky="w", padx=4)
combo = ttk.Combobox(frame_input, values=list(PARTICLES.keys()), state="readonly",
                     font=FONT, width=14)
combo.current(0)                        # по умолчанию первый элемент
combo.grid(row=0, column=1, padx=8)

# Кнопка расчёта
tk.Button(app, text="Рассчитать", font=FONT_BOLD,
          bg="#4CAF50", fg="white", command=rasschitat).pack(**PAD)

# Блок результатов
frame_result = tk.LabelFrame(app, text="Результаты", font=FONT_BOLD, padx=10, pady=8)
frame_result.pack(fill="x", padx=12, pady=6)

lbl_mass    = tk.Label(frame_result, text="Масса:                     —", font=FONT, anchor="w")
lbl_charge  = tk.Label(frame_result, text="Заряд:                     —", font=FONT, anchor="w")
lbl_spec    = tk.Label(frame_result, text="Удельный заряд:            —", font=FONT, anchor="w")
lbl_compton = tk.Label(frame_result, text="Комптоновская длина волны: —", font=FONT, anchor="w")

for lbl in (lbl_mass, lbl_charge, lbl_spec, lbl_compton):
    lbl.pack(fill="x")

# Кнопки сохранения текущей частицы
ttk.Separator(app, orient="horizontal").pack(fill="x", padx=12, pady=4)
tk.Label(app, text="Сохранить текущую частицу:", font=FONT).pack()

frame_save1 = tk.Frame(app)
frame_save1.pack(**PAD)
tk.Button(frame_save1, text="💾 Сохранить в .docx", font=FONT,
          command=sohranit_word).grid(row=0, column=0, padx=6)
tk.Button(frame_save1, text="💾 Сохранить в .xlsx", font=FONT,
          command=sohranit_excel).grid(row=0, column=1, padx=6)

# Кнопки сохранения всех частиц
tk.Label(app, text="Сохранить все три частицы:", font=FONT).pack()

frame_save2 = tk.Frame(app)
frame_save2.pack(**PAD)
tk.Button(frame_save2, text="📄 Все в .docx", font=FONT,
          command=sohranit_vse_word).grid(row=0, column=0, padx=6)
tk.Button(frame_save2, text="📊 Все в .xlsx", font=FONT,
          command=sohranit_vse_excel).grid(row=0, column=1, padx=6)

# ─── Запуск главного цикла ──────────────────────────────────────
app.mainloop()
