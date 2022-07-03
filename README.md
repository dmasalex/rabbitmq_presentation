Презентация RABBITMQ

1. Теория RABBITMQ (5 мин) - основные понятия, термины и тд.
   
2. Установка и запуск кролика:
   - brew install rabbitmq
   - brew services start rabbitmq
   
3. Знакомство с web-интерфейсом (морда кролика) - очереди, подключения и тд.
   - http://127.0.0.1:15672/
   
4. Создание проекта (виртуальное окружение), установка зависимостей:
   - python3 -m venv env && source env/bin/activate
   - pip install -r requirements.txt
   
5. Файл tasks.py - импорт celery, запуск 30шт. задач:
   - python tasks.py
   - queue, routing_key, priority
   - Отображение созданных задач в морде кролика.
   - запуск воркеров celery:
        - celery -A push_task worker -l info
   
6. Файл push_task.py - подключение к кролику, выполнение задач, показ результата в терминале:
    - python push_task.py
   
7. Финал, аплодисменты!
