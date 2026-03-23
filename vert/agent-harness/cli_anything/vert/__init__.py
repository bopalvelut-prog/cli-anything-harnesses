import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('vert running')
@cli.command()
def start(): click.echo('vert started')
if __name__ == '__main__': cli()
