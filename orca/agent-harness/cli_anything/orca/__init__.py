import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def scan(): click.echo('Orca scan')
@cli.command()
def alerts(): click.echo('Orca alerts')
if __name__ == '__main__': cli()
