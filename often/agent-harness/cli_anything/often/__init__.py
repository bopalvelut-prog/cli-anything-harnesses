import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('often running')
@cli.command()
def start(): click.echo('often started')
if __name__ == '__main__': cli()
