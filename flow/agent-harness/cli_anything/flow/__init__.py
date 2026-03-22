import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def account(): click.echo('Flow account')
@cli.command()
def transfer(): click.echo('Flow transfer')
if __name__ == '__main__': cli()
