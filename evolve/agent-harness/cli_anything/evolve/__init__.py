import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('evolve running')
@cli.command()
def start(): click.echo('evolve started')
if __name__ == '__main__': cli()
