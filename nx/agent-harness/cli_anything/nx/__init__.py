import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nx running')
@cli.command()
def start(): click.echo('nx started')
if __name__ == '__main__': cli()
