"""Data models for HTTP analysis."""

from dataclasses import dataclass, field
from typing import Optional, Dict, Any
from datetime import datetime


@dataclass
class TimingInfo:
    """Timing information for HTTP request."""
    dns_lookup: float = 0.0
    tcp_connect: float = 0.0
    tls_handshake: float = 0.0
    time_to_first_byte: float = 0.0
    total_time: float = 0.0


@dataclass
class RequestConfig:
    """Configuration for HTTP request."""
    url: str
    method: str = "GET"
    headers: Dict[str, str] = field(default_factory=dict)
    body: Optional[str] = None
    timeout: int = 30
    follow_redirects: bool = True


@dataclass
class ResponseData:
    """HTTP response data."""
    status_code: int
    headers: Dict[str, str]
    body: str
    url: str  # Final URL after redirects
    timing: TimingInfo
    timestamp: datetime = field(default_factory=datetime.now)
    redirect_count: int = 0


@dataclass
class Finding:
    """Analysis finding."""
    severity: str  # 'info', 'warning', 'error'
    category: str  # 'security', 'performance', 'headers'
    message: str
    details: Optional[str] = None


@dataclass
class AnalysisResult:
    """Complete analysis result."""
    request: RequestConfig
    response: ResponseData
    findings: list[Finding] = field(default_factory=list)
    
    def add_finding(self, severity: str, category: str, message: str, details: Optional[str] = None):
        """Add a finding to results."""
        self.findings.append(Finding(severity, category, message, details))