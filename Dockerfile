FROM python:3.14-slim

WORKDIR /app

# Avoid pip's progress-bar thread in constrained environments
ENV PIP_PROGRESS_BAR=off

# Install uv
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir uv

# Copy lock + metadata first for better layer caching
COPY pyproject.toml uv.lock ./

# Copy your actual application source too
COPY . .

# Install the project into the system environment
RUN uv sync --locked --no-dev

CMD ["uwsgi", "app.ini"]