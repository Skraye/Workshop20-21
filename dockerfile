FROM python:3.8
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /code/
USER worker
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
