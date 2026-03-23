import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gift running')
@cli.command()
def start(): click.echo('gift started')
if __name__ == '__main__': cli()
