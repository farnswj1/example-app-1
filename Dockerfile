# base image
FROM ghcr.io/astral-sh/uv:python3.13-bookworm

# set environment variables
ENV PYTHONUNBUFFERED=1

# expose port(s)
EXPOSE 8000

# set directory
WORKDIR /opt/app

# add application and install dependencies
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen
COPY . ./

# run the application
CMD ["uv", "run", "fastapi", "run", "main.py"]
