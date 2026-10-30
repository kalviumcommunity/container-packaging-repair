FROM python:3.12 AS build
WORKDIR /app
COPY . .
RUN python -m venv /opt/venv && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt
FROM python:3.12-slim
WORKDIR /app
COPY --from=build /opt/venv /wrong/venv
ENV PATH="/wrong/bin:$PATH"
COPY . .
EXPOSE 8080
CMD ["/opt/venv/bin/python", "app.py"]
