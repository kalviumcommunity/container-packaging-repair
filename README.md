# container-packaging-repair

Intentionally broken DevOps Foundation Module 4 starter. Only documented faults and incomplete review lines require repair. Read assessment before editing.

## Preparation

Fork https://github.com/kalviumcommunity/container-packaging-repair, clone YOUR fork and create fix/module4 branch. Free local Docker Engine/Compose, Git, terminal and PDF export only. Docker Desktop subject to its license; free Docker Engine on Linux is sufficient. No cloud account, billing, registry login, tokens, paid tools or Kubernetes cluster. Pull python:3.12-slim and python:3.12 before assessment. Host ports 18081-18084 and 19082 must be free. POSIX shell (Linux/macOS or prepared WSL); preparation and image downloads outside timer.

## Allowed edits

Dockerfile, .dockerignore. Keep routes, ports, application behaviour, fixtures and baseline unchanged except explicitly permitted temporary cache comment. Capture original failure before each repair. No bypasses or fabricated evidence.

## Required behaviour and commands

Required module src/banner.py must be included. Keep .git/.env/cache exclusions. Move dependency-only COPY and pip installation before builder source COPY. Keep pip --no-cache-dir. Runtime must copy venv to /opt/venv and put /opt/venv/bin first on PATH; use CMD ["python", "app.py"]. Keep both stages Python 3.12. This is six substantive Dockerfile operations across two tasks, not a from-scratch rewrite.

To isolate Task 1 from broken final runtime: docker build --target build -t helpdesk:builder . then docker run --rm helpdesk:builder python -c "from src.banner import NAME; print(NAME)". Capture missing-module failure before editing .dockerignore.

Cache proof: build builder once, add temporary comment to app.py, build builder again with --progress=plain, show dependency RUN CACHED, then restore app.py. No lasting app edit. After all repairs build Dockerfile.baseline as helpdesk:baseline and final Dockerfile as helpdesk:fixed. Compare actual image sizes on same machine; report bytes/percentage, no fixed expected savings. Both images must run same app. Baseline needs corrected .dockerignore too. Final run: docker run -d --name m4-q1 -e APP_MODE=production -p 18081:8080 helpdesk:fixed. Verify /health and /config. No external packages downloaded by pip.

## Evidence and submission

One PDF, three labelled task sections. Grade only task work and requested screenshot/written evidence. Repository/fork URLs, branch names and submission commit hashes are not required or graded. Show initial failures, actual diagnosis commands, complete corrected diff, successful checks and requested written lines. At least one real screenshot per task. No PR/video/ZIP. Written answers human-graded; static configuration alone is not runtime proof. Keep .env untracked. Wait for startup log/health state, not arbitrary immediate curl. Do not remove unrelated containers. Cleanup exercise containers only.
