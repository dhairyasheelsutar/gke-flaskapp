FROM python:3.7 
COPY . /app
WORKDIR /app
ENV PYTHONUNBUFFERED 0
RUN pip install -r requirements.txt 
EXPOSE 5000 
CMD ["python", "-u", "app.py"]
