# container-packaging-repair

Intentionally broken DevOps Foundation Module 4 starter. No solved implementation or completed review answers are supplied. Diagnose and repair only the assessment tasks.

## Preparation

Fork or clone https://github.com/kalviumcommunity/container-packaging-repair before assessment. Fork ownership is not graded. Use free local Docker Engine/Compose, Git and POSIX shell (Linux/macOS or prepared WSL). Docker Desktop subject to its license; Linux Docker Engine is sufficient. Pull python:3.12-slim and python:3.12 before assessment. Reserve exercise ports only. Preparation/download delays excluded. No cloud account, billing, registry login, real credentials, paid tools or Kubernetes needed.

## Allowed edits

Dockerfile, .dockerignore. Temporary app.py comment for Task 2 only; restore it before submission. Preserve all other source, routes, ports, fixtures and checks. No failure suppression or fabricated output. Existing run.sh tolerates absence of its old exercise container only; that cleanup is not an application-validation bypass.

## Required behaviour and commands

The application requires src/banner.py at runtime. Keep repository metadata, local .env and Python cache files out of the build context. The builder must install dependencies from requirements.txt in a layer reusable when only app.py changes. Keep pip --no-cache-dir and Python 3.12 in both stages.

Runtime contract: the virtual environment is available at /opt/venv; its interpreter is selected through PATH. Start app.py with that interpreter. Do not change application code, requirements or the supplied baseline. Infer the Dockerfile edits from this contract; no solved Dockerfile is supplied.

Isolate Task 1 using the existing build target:
```sh
docker build --target build -t helpdesk:builder .
docker run --rm helpdesk:builder python -c 'from src.banner import NAME; print(NAME)'
```
For Task 2 build the builder, temporarily append a comment to app.py, rebuild with --progress=plain, inspect dependency-layer caching, then restore app.py byte-for-byte. Compare the pre-repair and repaired source-change builds; do not change requirements.txt.

For Task 3 build Dockerfile.baseline as helpdesk:baseline and Dockerfile as helpdesk:fixed using the same corrected context and machine. Run each with APP_MODE=production; compare actual image sizes and report (baseline - fixed) / baseline * 100. No fixed expected percentage. Most savings here come from the slim runtime base, not an inherent guarantee of multi-stage builds. The two images must serve the same app.
```sh
docker run -d --name m4-q1 -e APP_MODE=production -p 18081:8080 helpdesk:fixed
curl -i http://localhost:18081/health
curl -i http://localhost:18081/config
docker exec m4-q1 python -c 'import sys; print(sys.executable)'
```
Capture the original final-runtime startup failure before applying Task 3 repairs. Cleanup only containers created for this exercise.

## Evidence and submission

Follow assessment's three tasks. One PDF, three labelled task sections, at least one real terminal screenshot per task, requested findings and cause/fix/result captions. Include complete corrected diff of permitted files once. Show original failures and final checks only as requested by each task. Grade only those tasks and evidence (6 + 7 + 7 = 20). Repository/fork URLs, fork ownership, branch names and submission commit hashes are not required or graded. Technical image IDs remain required where tasks ask for them. Standalone instructor evidence is valid under the same technical criteria. Written findings are manually assessed; local evidence does not prove Cloud Run deployment. No PR, video or ZIP. Cleanup only exercise containers; never expose real credentials.
