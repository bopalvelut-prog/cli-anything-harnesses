import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def account(): click.echo('NEM account')
@cli.command()
def transfer(): click.echo('NEM transfer')
if __name__ == '__main__': cli()
