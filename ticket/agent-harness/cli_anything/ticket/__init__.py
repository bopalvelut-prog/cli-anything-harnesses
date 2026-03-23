import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ticket running')
@cli.command()
def start(): click.echo('ticket started')
if __name__ == '__main__': cli()
