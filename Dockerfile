FROM ubuntu

ARG pass

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python python-pip python-dev && pip install --upgrade pip

RUN apt-get update -y && apt-get install git -y

RUN wget -qO- https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

RUN apt-get -y update
RUN apt-get install -y firefox

RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/75.0.3770.90/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

RUN wget -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
RUN tar xvzf /tmp/geckodriver.tar.gz -C /usr/local/bin/

RUN pip install pytest
RUN pip install selenium

RUN git clone https://BahrmaLe:$pass@github.com/BahrmaLe/otus_python_homework.git /otus_python_homework


WORKDIR /otus_python_homework


CMD ["/bin/bash"]