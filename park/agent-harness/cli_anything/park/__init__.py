import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('park running')
@cli.command()
def start(): click.echo('park started')
if __name__ == '__main__': cli()
