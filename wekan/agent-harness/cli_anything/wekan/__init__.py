import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('Wekan running')
@cli.command()
def boards(): click.echo('Wekan boards')
if __name__ == '__main__': cli()
