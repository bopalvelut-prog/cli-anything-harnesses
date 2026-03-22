import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('image')
def scan(image): subprocess.run(['grype', image])
if __name__ == '__main__': cli()
