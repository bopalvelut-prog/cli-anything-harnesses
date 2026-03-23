import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('suddenly running')
@cli.command()
def start(): click.echo('suddenly started')
if __name__ == '__main__': cli()
