import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def account(): click.echo('MultiversX account')
@cli.command()
def transfer(): click.echo('MultiversX transfer')
if __name__ == '__main__': cli()
