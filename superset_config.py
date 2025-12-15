import os

# Un secret key bien aléatoire (exemple, à changer si tu veux)
SECRET_KEY = "f0c8a5b4f7a9442cb5f4e7ce9b7f1e90b4c31d7f5c2a0dd4e7a8b3c9f1d2e3a9"
FEATURE_FLAGS = {
    "DASHBOARD_FILTERS_EXPERIMENTAL": True,
    "DASHBOARD_NATIVE_FILTERS": True,
    "DASHBOARD_CROSS_FILTERS": True,      # optionnel
    # "DASHBOARD_NATIVE_FILTERS_SET": True,  # optionnel 
    "ENABLE_TEMPLATE_PROCESSING": True,   # paramètres/jinja
}