# LLM Guard API

A simple `fastapi`-based API to run LLM Guard checks.

## Installation

1. Clone the repo and move to the `examples/api` folder

2. Install dependencies (preferably in a virtual environment)

```sh
pip install -r requirements.txt
```

Or you can use Makefile

```sh
make install
```

3. Run the API:

```sh
make run
```

Or you can run it using Docker:

```sh
make run-docker
```

## Configuration

It can be configured using environment variables:

- `DEBUG` (bool): Enable debug mode
- `CACHE_MAX_SIZE` (int): Maximum number of items in the cache. Default is unlimited.
- `CACHE_TTL` (int): Time in seconds after which a cached item expires. Default is 1 hour.

Also, you can configure scanners in `config.yml` referring to their names and parameters.

## Deploy Docker

### Download Docker images
docker pull laiyer/llm-guard-api

#### Run containers with default ports
docker run -d -p 8001:8000 laiyer/llm-guard-api:latest