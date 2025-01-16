FROM python:3.12.8-slim-bullseye
WORKDIR /user/local/app

COPY src ./src

CMD ["python", "-m", "src.app"]
