import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('researcher running')
@cli.command()
def start(): click.echo('researcher started')
if __name__ == '__main__': cli()
