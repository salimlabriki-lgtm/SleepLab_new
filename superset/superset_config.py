SECRET_KEY = "change-me-please"
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://superset:superset@superset-db:5432/superset"
SQLALCHEMY_TRACK_MODIFICATIONS = False
FEATURE_FLAGS = {
    "DASHBOARD_NATIVE_FILTERS": True,
    "DASHBOARD_CROSS_FILTERS": True,
    "ENABLE_TEMPLATE_PROCESSING": True,
}
