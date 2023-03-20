FROM python

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

#RUN pip install mysql-connector
#RUN pip install python-dotenv

ENV DB_HOST ""
ENV DB_PORT ""
ENV DB_USERNAME ""
ENV DB_PASSWORD ""
ENV HOSTNAME ""
ENV HOST_FRIENDLY_NAME ""
ENV MOUNT_POINTS ""

ENV DELAY_SEC ""
ENV DELAY_ON_FAIL_SEC ""

VOLUME /user/config

RUN mkdir /code
COPY agent/homelab_monitoring_agent/*.py /code/

WORKDIR /code

ENTRYPOINT [ "python3", "monitor.py" ]
