import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('BCH node')
@cli.command()
def wallet(): click.echo('BCH wallet')
if __name__ == '__main__': cli()
