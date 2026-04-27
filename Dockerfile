FROM python
WORKDIR /src
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5500
CMD ["python", "app.py"]