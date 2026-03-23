import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('river running')
@cli.command()
def start(): click.echo('river started')
if __name__ == '__main__': cli()
