"""
Website Package.

This package contains the Flask application and its configurations.
"""

from .app import create_app

app = create_app()
