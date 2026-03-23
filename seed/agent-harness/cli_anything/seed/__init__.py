import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('seed running')
@cli.command()
def start(): click.echo('seed started')
if __name__ == '__main__': cli()
