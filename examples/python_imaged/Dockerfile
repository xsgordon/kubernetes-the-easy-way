FROM fedora:latest
EXPOSE 8080

LABEL MAINTAINER="sgordon@redhat.com"

RUN dnf update -y && dnf install -y python && dnf clean all

COPY python_imaged.py .
COPY Cat_Melon.jpg .

ENTRYPOINT [ "python", "./python_imaged.py" ]
