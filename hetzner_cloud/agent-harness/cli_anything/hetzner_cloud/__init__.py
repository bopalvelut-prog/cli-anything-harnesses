import click
@click.group()
def cli(): pass
@cli.command()
def servers(): click.echo('Cloud servers')
@cli.command()
def volumes(): click.echo('Cloud volumes')
if __name__ == '__main__': cli()
