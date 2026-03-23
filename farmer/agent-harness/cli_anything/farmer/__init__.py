import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('farmer running')
@cli.command()
def start(): click.echo('farmer started')
if __name__ == '__main__': cli()
