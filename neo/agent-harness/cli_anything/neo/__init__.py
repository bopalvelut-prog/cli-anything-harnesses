import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def account(): click.echo('NEO account')
@cli.command()
def transfer(): click.echo('NEO transfer')
if __name__ == '__main__': cli()
