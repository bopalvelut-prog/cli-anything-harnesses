import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rotate running')
@cli.command()
def start(): click.echo('rotate started')
if __name__ == '__main__': cli()
