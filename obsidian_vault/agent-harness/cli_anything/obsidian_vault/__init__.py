import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def notes(): click.echo('Vault notes')
@cli.command()
def graph(): click.echo('Graph view')
if __name__ == '__main__': cli()
