# Stage 1: Build dependencies
FROM python:3.9-slim AS build

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Copy only necessary parts for the final image
FROM python:3.9-slim

WORKDIR /app
COPY --from=build /app /app

EXPOSE 443
USER root

ENTRYPOINT ["python", "main.py"]