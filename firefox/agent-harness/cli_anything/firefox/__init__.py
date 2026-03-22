
import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('url')
def open(url): subprocess.run(['firefox', url]); click.echo(f'Opened: {url}')
@cli.command()
@click.argument('url')
def headless(url): click.echo(f'Headless: {url}')
if __name__ == '__main__': cli()
