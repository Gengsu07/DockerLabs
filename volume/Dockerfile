FROM python:latest
ENV APP_LOGS = /logs

RUN mkdir ${APP_LOGS}
RUN mkdir app
COPY /log /${APP_LOGS}
COPY /app app

WORKDIR /app
VOLUME ${APP_LOGS}

RUN pip install -r requirements.txt --no-cache
EXPOSE 8501

ENTRYPOINT [ "streamlit","run" ]
CMD ["app.py"]