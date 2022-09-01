FROM python:latest

RUN mkdir app
COPY /app app

EXPOSE 8501
WORKDIR /app
RUN pip install -r requirements.txt --no-cache

ENTRYPOINT [ "streamlit","run" ]
CMD ["app.py"]