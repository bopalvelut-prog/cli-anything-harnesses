import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('massive running')
@cli.command()
def start(): click.echo('massive started')
if __name__ == '__main__': cli()
