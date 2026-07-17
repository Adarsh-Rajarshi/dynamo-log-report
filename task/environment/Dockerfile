# Base image pinned by digest for reproducibility (python:3.12-slim).
FROM python:3.12-slim@sha256:57cd7c3a7a273101a6485ba99423ee568157882804b1124b4dd04266317710de

# Test tooling for the verifier (baked into the image so the verifier needs no network).
RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

# Only the task input ships in the agent image. The reference solution is NOT copied here.
COPY access.log /app/access.log
