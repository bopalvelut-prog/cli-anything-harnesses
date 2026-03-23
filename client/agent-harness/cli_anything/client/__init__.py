import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('client running')
@cli.command()
def start(): click.echo('client started')
if __name__ == '__main__': cli()
