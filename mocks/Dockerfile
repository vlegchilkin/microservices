# syntax=docker/dockerfile:1.2
FROM localhost:5001/docker-python:3.9 as builder
ARG EXTRA_INDEX_URLS=""

WORKDIR /app
COPY pyproject.toml poetry.lock* README.md ./
COPY mocks ./mocks/

USER worker
RUN --mount=type=secret,id=pip.conf,dst=/home/worker/.pip/pip.conf,uid=1000 \
    pip install --user --force-reinstall $EXTRA_INDEX_URLS .

FROM localhost:5001/docker-python:3.9
COPY --from=builder /home/worker/.local /home/worker/.local

EXPOSE 8080
CMD ["python", "-m", "mocks.service"]
