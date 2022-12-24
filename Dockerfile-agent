FROM python:3.9

RUN pip install mysql-connector

ENV DB_HOST ""
ENV DB_PORT ""
ENV DB_USERNAME ""
ENV DB_PASSWORD ""
ENV HOSTNAME ""
ENV HOST_FRIENDLY_NAME ""
ENV MOUNT_POINTS ""

RUN mkdir /code
COPY agent/homelab_monitoring_agent/*.py /code/

WORKDIR /code

ENTRYPOINT [ "python3", "monitor.py" ]
