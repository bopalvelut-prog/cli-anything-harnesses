import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('url')
def download(url): subprocess.run(['aria2c', url])
@cli.command()
@click.argument('urls', nargs=-1)
def multi(urls): subprocess.run(['aria2c'] + list(urls))
if __name__ == '__main__': cli()
