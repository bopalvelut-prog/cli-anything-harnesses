import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('url')
def download(url): subprocess.run(['wget', url])
@cli.command()
def mirror(): subprocess.run(['wget', '--mirror', '-p', '--convert-links', '-P', './wget', '.'])
if __name__ == '__main__': cli()
