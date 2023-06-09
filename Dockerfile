FROM python:3.11
RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . .
RUN chmod a+x docker/*.sh