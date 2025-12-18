# superset/superset_config.py
#
# Objectif:
# - Forcer Superset à utiliser Postgres (superset-db) comme metadata DB
#   => persistance des users / roles / dashboards / connections
# - Activer les flags dont tu as besoin

# IMPORTANT: doit matcher SUPERSET_SECRET_KEY dans docker-compose
SECRET_KEY = "change-me-please"

# IMPORTANT: metadata DB Superset (sinon Superset retombe sur SQLite et tu perds tout)
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://superset:superset@superset-db:5432/superset"

# Optionnel mais propre (évite du bruit)
SQLALCHEMY_TRACK_MODIFICATIONS = False

FEATURE_FLAGS = {
    "DASHBOARD_FILTERS_EXPERIMENTAL": True,
    "DASHBOARD_NATIVE_FILTERS": True,
    "DASHBOARD_CROSS_FILTERS": True,
    "ENABLE_TEMPLATE_PROCESSING": True,
}
