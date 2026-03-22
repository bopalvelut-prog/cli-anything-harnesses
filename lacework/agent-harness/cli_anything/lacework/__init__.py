import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def scan(): click.echo('Lacework scan')
@cli.command()
def alerts(): click.echo('Lacework alerts')
if __name__ == '__main__': cli()
