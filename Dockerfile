FROM ubuntu:latest
LABEL authors="statiin"

ENTRYPOINT ["top", "-b"]