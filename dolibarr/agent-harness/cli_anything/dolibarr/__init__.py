import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('Dolibarr started')
@cli.command()
def modules(): click.echo('Dolibarr modules')
if __name__ == '__main__': cli()
