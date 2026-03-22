import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('Burp Suite started')
@cli.command()
def proxy(): click.echo('Proxy running on :8080')
if __name__ == '__main__': cli()
