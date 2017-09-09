FROM fedora:latest
EXPOSE 8080

LABEL MAINTAINER="sgordon@redhat.com"

RUN dnf update -y && dnf install -y python && dnf clean all

COPY python_httpd.py .

ENTRYPOINT [ "python", "./python_httpd.py" ]
