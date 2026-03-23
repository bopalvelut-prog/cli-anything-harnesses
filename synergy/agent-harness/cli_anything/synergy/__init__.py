import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('synergy running')
@cli.command()
def start(): click.echo('synergy started')
if __name__ == '__main__': cli()
