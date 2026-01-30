"""
OpenSpecimen Python API Client
A lightweight Python client for interacting with the OpenSpecimen REST API.

This package provides tools for:
- Session authentication with OpenSpecimen
- Executing AQL queries
- Retrieving results as JSON or pandas DataFrames
"""

from .api_query import ApiQuery
from .client import Client

# Package metadata
__version__ = "0.1.1"
__author__ = "Stefan Bartels"
__email__ = "email@biobits.eu"
__license__ = "MIT"
__all__ = ['ApiQuery', 'Client', '__version__']
