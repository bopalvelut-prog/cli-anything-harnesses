import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Dogecoin node')
@cli.command()
def wallet(): click.echo('Dogecoin wallet')
if __name__ == '__main__': cli()
