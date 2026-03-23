import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('recovery running')
@cli.command()
def start(): click.echo('recovery started')
if __name__ == '__main__': cli()
