import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('unmark running')
@cli.command()
def start(): click.echo('unmark started')
if __name__ == '__main__': cli()
