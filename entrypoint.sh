
#!/bin/sh
set -e

python -c "from run import app; from app.seed import initialize_database; ctx = app.app_context(); ctx.push(); initialize_database(); ctx.pop()"

exec gunicorn --workers 2 --bind 0.0.0.0:5000 run:app
