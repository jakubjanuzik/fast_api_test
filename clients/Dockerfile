FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN pip install -U pip
COPY .env .env
COPY start-reload.sh /start-reload.sh
COPY requires.txt requires.txt
RUN pip install -r requires.txt
COPY ./app /app
RUN chmod +x /start-reload.sh
CMD ["/start-reload.sh"]

