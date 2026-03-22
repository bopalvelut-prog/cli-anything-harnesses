import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def ping(): click.echo('ZMQ ping')
@cli.command()
def stats(): click.echo('ZMQ statistics')
if __name__ == '__main__': cli()
