"""Build HTTP requests from CLI options."""

from typing import Dict, Optional
from urllib.parse import urlparse
from .models import RequestConfig


class RequestBuilder:
    """Build HTTP request configurations."""
    
    def __init__(self, url: str):
        self.url = self._validate_url(url)
        self.method = "GET"
        self.headers: Dict[str, str] = {}
        self.body: Optional[str] = None
        self.timeout = 30
        self._follow_redirects = True 
    
    def _validate_url(self, url: str) -> str:
        """Validate and normalize URL."""
        if not url.startswith(('http://', 'https://')):
            url = f'https://{url}'
        
        parsed = urlparse(url)
        if not parsed.netloc:
            raise ValueError(f"Invalid URL: {url}")
        
        return url
    
    def with_method(self, method: str) -> 'RequestBuilder':
        """Set HTTP method."""
        self.method = method.upper()
        return self
    
    def with_header(self, key: str, value: str) -> 'RequestBuilder':
        """Add a header."""
        self.headers[key] = value
        return self
    
    def with_headers(self, headers: Dict[str, str]) -> 'RequestBuilder':
        """Add multiple headers."""
        self.headers.update(headers)
        return self
    
    def with_body(self, body: str) -> 'RequestBuilder':
        """Set request body."""
        self.body = body
        return self
    
    def with_timeout(self, timeout: int) -> 'RequestBuilder':
        """Set timeout in seconds."""
        self.timeout = timeout
        return self
    
    def follow_redirects(self, follow: bool = True) -> 'RequestBuilder':
        """Set whether to follow redirects."""
        self._follow_redirects = follow
        return self
    
    def build(self) -> RequestConfig:
        """Build the request configuration."""
        return RequestConfig(
            url=self.url,
            method=self.method,
            headers=self.headers, 
            body=self.body,
            timeout=self.timeout,
            follow_redirects=self._follow_redirects
        )