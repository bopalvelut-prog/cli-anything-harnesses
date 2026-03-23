import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('consumer running')
@cli.command()
def start(): click.echo('consumer started')
if __name__ == '__main__': cli()
