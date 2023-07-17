FROM python:3.8
WORKDIR /src/
ENV PYTHONDONTWRITEBYTEECODE=1
ENV PYTHONUNBUFFRED=1
COPY requirments.txt /src/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirments.txt
COPY . /src/
