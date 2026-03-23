import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tyr running')
@cli.command()
def start(): click.echo('tyr started')
if __name__ == '__main__': cli()
