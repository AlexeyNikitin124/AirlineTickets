- дождаться установки всех библиотек и сборки проекта (`Installing the current project: project (0.1.0)`)
- в терминале прописать docker compose up
- дождаться пока база данных будет готова (`database system is ready to accept connections`)
- подключиться к базе (DBeaver, DataGrip, PGadmin и т.д.)
- выполнить в базе скрипты из папки scripts для создания схемы и таблицы
- запустить файл src/project/main.py
- При успешном запуске будет написано:
  - `INFO:     Application startup complete.`

- обратите внимание на файл src/project/core/config.py
- в нем руками перебиты значения из переменных сред из .env файла
- это временное решение, пока бэкенд не будет контейнеризирован

- Swagger:
Swagger:
- после успешного запуска приложения, по адресу http://localhost:8000/docs будет доступен swagger