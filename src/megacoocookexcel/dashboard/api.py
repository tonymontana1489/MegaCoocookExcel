"""
Dashboard API - Sprint 3.6
"""

class DashboardAPI:

    def ping(self):
        return {
            "success": True,
            "message": "Python API erreichbar."
        }

    def version(self):
        return "Sprint 3.6"
