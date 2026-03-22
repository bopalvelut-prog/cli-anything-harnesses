import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('image')
def scan(image): click.echo(f'Scanning {image}')
if __name__ == '__main__': cli()
