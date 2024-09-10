FROM python:3.12.6-slim AS base

# Python settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

# Other settings
ENV CODE_PATH=/code

# Install OS packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR $CODE_PATH

FROM base AS builder

# Poetry settings
ENV POETRY_VERSION=1.5.1
ENV POETRY_HOME=/etc/poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH=$POETRY_HOME/bin:$PATH

# Install dependencies
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root

FROM base

# Copy Grimoirebots files
COPY . ./

# Setup environment
COPY --from=builder $CODE_PATH/.venv ./.venv
ENV PATH=$CODE_PATH/.venv/bin:$PATH

# Collect static files
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "4", "grimoirebots.wsgi"]
