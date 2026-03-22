import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Clair running')
@cli.command()
def scan(): click.echo('Clair scan')
if __name__ == '__main__': cli()
