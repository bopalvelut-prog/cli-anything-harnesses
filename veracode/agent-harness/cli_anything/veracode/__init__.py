import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def scan(): click.echo('Veracode scan')
@cli.command()
def report(): click.echo('Veracode report')
if __name__ == '__main__': cli()
