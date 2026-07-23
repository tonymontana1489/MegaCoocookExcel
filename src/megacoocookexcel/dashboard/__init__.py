"""
Dashboard package.
"""

from .api import app
from .bridge import DashboardBridge

__all__ = [
    "app",
    "DashboardBridge",
]