FROM python
RUN apt-update -y
RUN apt install -y python3pip \ 
	python-dev build-essential apt-utils 
COPY ./app
WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY .  .
EXPOSE 5000
CMD ["python","app.py"]