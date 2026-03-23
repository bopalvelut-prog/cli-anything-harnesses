import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('handle running')
@cli.command()
def start(): click.echo('handle started')
if __name__ == '__main__': cli()
