"""CLI entry point for HTTP Analyzer."""

import click
from rich.console import Console
from rich.table import Table

from .client import HTTPClient
from .request_builder import RequestBuilder

console = Console()


@click.group()
@click.version_option(version="0.1.0", prog_name="http-analyzer")
def main() -> None:
    """HTTP Analyzer CLI - Analyze HTTP requests and responses."""
    pass


@main.command()
@click.argument("url")
@click.option("--method", "-m", default="GET", help="HTTP method to use")
@click.option("--header", "-H", multiple=True, help="Custom header (key:value)")
@click.option("--data", "-d", help="Request body data")
@click.option("--timeout", "-t", default=30, help="Request timeout in seconds")
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
def analyze(url: str, method: str, header: tuple, data: str, timeout: int, verbose: bool) -> None:
    """Analyze an HTTP request to URL."""
    try:
        # Build request
        console.print(f"[bold green]Analyzing:[/bold green] {url}")
        
        builder = RequestBuilder(url).with_method(method).with_timeout(timeout)
        
        # Add custom headers
        for h in header:
            if ':' in h:
                key, value = h.split(':', 1)
                builder.with_header(key.strip(), value.strip())
        
        # Add body if provided
        if data:
            builder.with_body(data)
        
        config = builder.build()
        
        # Execute request
        client = HTTPClient()
        with console.status("[bold yellow]Making request...", spinner="dots"):
            response = client.execute(config)
        
        # Display results
        console.print(f"\n[bold]Status:[/bold] {response.status_code}")
        console.print(f"[bold]Final URL:[/bold] {response.url}")
        
        if response.redirect_count > 0:
            console.print(f"[bold]Redirects:[/bold] {response.redirect_count}")
        
        console.print(f"[bold]Time:[/bold] {response.timing.total_time:.2f}ms")
        
        # Headers table
        if verbose:
            console.print("\n[bold]Response Headers:[/bold]")
            headers_table = Table(show_header=True, header_style="bold cyan")
            headers_table.add_column("Header")
            headers_table.add_column("Value")
            
            for key, value in response.headers.items():
                headers_table.add_row(key, value)
            
            console.print(headers_table)
            
            # Body preview
            console.print(f"\n[bold]Body Length:[/bold] {len(response.body)} bytes")
            if len(response.body) < 500:
                console.print(f"\n[dim]{response.body}[/dim]")
            else:
                console.print(f"\n[dim]{response.body[:500]}...[/dim]")
        
    except ValueError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
    except Exception as e:
        console.print(f"[bold red]Request failed:[/bold red] {e}")


@main.command()
def version() -> None:
    """Show version information."""
    console.print("[bold]HTTP Analyzer CLI[/bold] v0.1.0")


if __name__ == "__main__":
    main()