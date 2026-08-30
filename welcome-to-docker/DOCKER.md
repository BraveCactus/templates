# Docker: сборка и запуск

```bash
# Собрать образ
docker build -t welcome-to-docker .

# Запустить контейнер с bind mount папки ./data в /data
docker run -d --name docker_container1 -e GREETING="Hello" -p 5000:5000 -v "${PWD}/data:/data" welcome-to-docker

# Остановить
docker stop docker_container1

# Удалить 
docker rm docker_container1
```

Счётчик пишется в `data/counter.txt` на хосте.