#!/usr/bin/env python3
"""
HealthMonitor - System health monitoring and alerting.
"""

import psutil
from typing import Dict, List
from datetime import datetime

class HealthMonitor:
    """Monitor system health."""
    def __init__(self):
        self.alerts = []
    
    def get_cpu_usage(self) -> float:
        """Get CPU usage percentage."""
        return psutil.cpu_percent(interval=1)
    
    def get_memory_usage(self) -> Dict:
        """Get memory usage."""
        mem = psutil.virtual_memory()
        return {
            "total": mem.total,
            "available": mem.available,
            "used": mem.used,
            "percent": mem.percent
        }
    
    def get_disk_usage(self, path: str = "/") -> Dict:
        """Get disk usage."""
        disk = psutil.disk_usage(path)
        return {
            "total": disk.total,
            "used": disk.used,
            "free": disk.free,
            "percent": (disk.used / disk.total) * 100
        }
    
    def check_health(self, cpu_threshold: float = 80.0, memory_threshold: float = 80.0) -> Dict:
        """Check overall system health."""
        cpu = self.get_cpu_usage()
        memory = self.get_memory_usage()
        
        issues = []
        if cpu > cpu_threshold:
            issues.append(f"High CPU usage: {cpu}%")
        if memory["percent"] > memory_threshold:
            issues.append(f"High memory usage: {memory['percent']}%")
        
        return {
            "status": "healthy" if not issues else "unhealthy",
            "cpu_usage": cpu,
            "memory_usage": memory["percent"],
            "issues": issues,
            "timestamp": datetime.now().isoformat()
        }

if __name__ == "__main__":
    monitor = HealthMonitor()
    print("HealthMonitor initialized")
