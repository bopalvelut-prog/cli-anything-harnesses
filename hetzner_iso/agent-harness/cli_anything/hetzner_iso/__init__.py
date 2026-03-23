import click
@click.group()
def cli(): pass
@cli.command()
def list(): click.echo('ISOs')
@cli.command()
def attach(): click.echo('Attach ISO')
if __name__ == '__main__': cli()
