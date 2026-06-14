# Домашнее задание №3
Проект создает данные о студентах, а затем строит отчёт
Выполняется все это при помощи двух различных Docker контэйнеров

## Использование

### Генератор данных
```bash
./run.sh build_generator   # собрать образ generator
./run.sh run_generator     # запустить generator
./run.sh create_local_data # запустить generator и сохранить результат в local_data/data.csv 
```

### Аналитик данных
```bash
./run.sh build_reporter    # собрать образ reporrter
./run.sh run_reporter      # запустить reporter
```

### Вспомогательные команды
```bash
./run.sh structure         # вывести структуру проекта
./run.sh clear_data        # очистить data/
./run.sh inside_generator  # показать содержимое внутри контейнера generator
./run.sh inside_reporter   # показать содержимое внутри контейнера reporter
```
