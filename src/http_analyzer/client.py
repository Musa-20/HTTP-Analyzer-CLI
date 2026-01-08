"""HTTP client for making requests and capturing timing."""

import time
import httpx
from typing import Optional
from .models import RequestConfig, ResponseData, TimingInfo


class HTTPClient:
    """HTTP client with detailed timing capture."""
    
    def __init__(self):
        self.session: Optional[httpx.Client] = None
    
    def execute(self, config: RequestConfig) -> ResponseData:
        """Execute HTTP request and capture response data."""
        timing = TimingInfo()
        redirect_count = 0
        
        # Create client with custom event hooks for timing
        with httpx.Client(
            follow_redirects=config.follow_redirects,
            timeout=config.timeout  
        ) as client:
            # Capture start time
            start_time = time.perf_counter()
            
            try:
                # Make request
                response = client.request(
                    method=config.method,
                    url=config.url,
                    headers=config.headers,
                    content=config.body.encode() if config.body else None
                )
                
                # Calculate total time
                end_time = time.perf_counter()
                timing.total_time = (end_time - start_time) * 1000 
                
                # Count redirects
                redirect_count = len(response.history)  
                
                # Extract response data
                return ResponseData(
                    status_code=response.status_code,
                    headers=dict(response.headers), 
                    body=response.text,
                    url=str(response.url),
                    timing=timing,
                    redirect_count=redirect_count
                )
                
            except httpx.TimeoutException as e:
                raise Exception(f"Request timeout after {config.timeout}s: {str(e)}")
            except httpx.RequestError as e:  
                raise Exception(f"Request failed: {str(e)}")
    
    def execute_with_timing(self, config: RequestConfig) -> ResponseData:
        """Execute with detailed timing breakdown."""
        # For now, basic timing - we can enhance this later with connection pooling
        # and more granular timing (DNS, TCP, TLS) using custom transport
        return self.execute(config)