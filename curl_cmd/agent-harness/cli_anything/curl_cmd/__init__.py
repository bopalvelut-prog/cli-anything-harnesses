import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('url')
def get(url): subprocess.run(['curl', '-s', url])
@cli.command()
@click.argument('url')
def head(url): subprocess.run(['curl', '-I', url])
if __name__ == '__main__': cli()
