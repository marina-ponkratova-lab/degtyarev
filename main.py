import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
import re

API_KEY = 'YOUR_API_KEY'  # Замените на свой ключ

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.history_file = 'history.json'
        self.history = self.load_history()
        self.currencies = ['USD', 'EUR', 'GBP', 'JPY', 'RUB']
        self.create_widgets()
        self.update_history_table()

    def create_widgets(self):
        # ... (остальной код виджетов без изменений) ...

    def load_history(self):
        try:
            with open(self.history_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_history(self):
        with open(self.history_file, 'w') as f:
            json.dump(self.history, f)

    def update_history_table(self):
        for i in self.history_tree.get_children():
            self.history_tree.delete(i)
        for entry in self.history:
            self.history_tree.insert('', 'end', values=(
                entry['from'], entry['to'], entry['amount'], entry['result'], entry['rate']
            ))

    def validate_input(self):
        amount = self.amount_entry.get().replace(',', '.').strip()
        # Удаляем пробелы и неразрывные пробелы
        amount = amount.replace(' ', '').replace(' ', '')
        if not re.match(r'^\d+(\.\d+)?$', amount) or float(amount) <= 0:
            messagebox.showerror("Ошибка", "Сумма должна быть положительным числом")
            return False, None
        return True, float(amount)

    def get_rate(self, from_cur, to_cur):
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{from_cur}/{to_cur}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data['conversion_rate']
        except Exception as e:
            messagebox.showerror("Ошибка API", f"Не удалось получить курс: {e}")
            return None

    def convert(self):
        is_valid, amount = self.validate_input()
        if not is_valid:
            return

        from_cur = self.from_currency.get()
        to_cur = self.to_currency.get()

        rate = self.get_rate(from_cur, to_cur)
        if rate is None:
            return

        result = round(amount * rate, 2)
        self.result_label.config(text=f"Результат: {result} {to_cur}")

        entry = {
            "from": from_cur,
            "to": to_cur,
            "amount": amount,
            "result": result,
            "rate": rate,
            "timestamp": int(requests.get("http://worldtimeapi.org/api/ip").json()['unixtime'])
        }
        self.history.append(entry)
        self.save_history()
        self.update_history_table()

# Точка входа
if __name__ == '__main__':
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
