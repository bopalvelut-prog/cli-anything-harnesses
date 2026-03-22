import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def wallet(): click.echo('TON wallet')
@cli.command()
def transfer(): click.echo('TON transfer')
if __name__ == '__main__': cli()
