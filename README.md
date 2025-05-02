# test_task_telecom
test task for telecom team

## Task 1 - python-скрипт
Простой скрипт, который в цикле 5 раз обращается к сайту, и ждет случайный response code. В случа 4хх или 5хх кода ответа генерирует исключение.

## Task2 - работа с Docker
Составил простой Dockerfile. Для сборки образа из корневой директории запустить `docker build -t app -f task_2/Dockerfile .`.

Для запуска контейнера `docker run --name python_app app`.

Для просмотра логов контейнера можно использовать `docker logs python_app`



