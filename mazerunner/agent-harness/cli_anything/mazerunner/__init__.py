import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mazerunner running')
@cli.command()
def start(): click.echo('mazerunner started')
if __name__ == '__main__': cli()
