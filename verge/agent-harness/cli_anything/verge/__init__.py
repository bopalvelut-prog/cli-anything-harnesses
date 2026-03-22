import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Verge node')
@cli.command()
def wallet(): click.echo('Verge wallet')
if __name__ == '__main__': cli()
