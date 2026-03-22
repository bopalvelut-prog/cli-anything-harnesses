import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Terra 2.0 node')
@cli.command()
def wallet(): click.echo('Terra 2.0 wallet')
if __name__ == '__main__': cli()
