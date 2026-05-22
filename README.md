# ДЗ4 — MySQL у Docker + Titanic dataset

## Запуск

1. Клонувати репозиторій:
   git clone https://github.com/drvlada/PfDS_HW4.git
   cd PfDS_HW4

2. Підняти базу даних:
   docker compose up -d

3. Зачекати поки MySQL ініціалізується, потім:
   pip install -r requirements.txt
   python main.py

## Очікуваний результат
DataFrame з 891 рядком і 12 колонками у терміналі.