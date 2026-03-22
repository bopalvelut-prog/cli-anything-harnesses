import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('url')
def download(url): subprocess.run(['gallery-dl', url])
if __name__ == '__main__': cli()
