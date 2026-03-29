FROM python:3.14-slim

WORKDIR /app

# Install uv from the official uv image, not via pip
COPY --from=ghcr.io/astral-sh/uv:0.11.2 /uv /uvx /bin/

# Tell uv to use system Python in the container
ENV UV_SYSTEM_PYTHON=1

# Copy metadata first for layer caching
COPY pyproject.toml uv.lock ./

# Install only dependencies first
RUN uv pip install --system -r pyproject.toml

# Copy app source
COPY . .

# Install the project itself into system Python
RUN uv pip install --system .

CMD ["uwsgi", "app.ini"]