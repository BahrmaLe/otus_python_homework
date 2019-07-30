FROM ubuntu

ARG pass

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python python-pip python-dev && pip install --upgrade pip

RUN apt-get update -y && apt-get install git -y

RUN pip install pytest
RUN pip install selenium

RUN git clone https://BahrmaLe:$pass@github.com/BahrmaLe/otus_python_homework.git /otus_python_homework


WORKDIR /otus_python_homework


CMD ["/bin/bash"]