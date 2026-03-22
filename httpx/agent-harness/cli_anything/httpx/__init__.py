import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('url')
def probe(url): subprocess.run(['httpx', '-u', url])
@cli.command()
@click.argument('url')
def title(url): subprocess.run(['httpx', '-u', url, '-title'])
if __name__ == '__main__': cli()
