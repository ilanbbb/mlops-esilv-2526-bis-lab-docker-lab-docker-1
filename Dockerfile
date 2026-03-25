FROM python:3.11-slim

WORKDIR /app

ENV CURRENT_ENVIRONMENT=DEV

COPY app/back/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app/back ./back
COPY app/front ./front

EXPOSE 5000

CMD ["python", "back/app.py"]