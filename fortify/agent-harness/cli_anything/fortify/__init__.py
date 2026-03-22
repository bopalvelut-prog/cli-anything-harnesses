import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def scan(): click.echo('Fortify scan')
@cli.command()
def report(): click.echo('Fortify report')
if __name__ == '__main__': cli()
