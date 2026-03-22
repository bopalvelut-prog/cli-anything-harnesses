import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Dash node')
@cli.command()
def wallet(): click.echo('Dash wallet')
if __name__ == '__main__': cli()
