import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('route running')
@cli.command()
def start(): click.echo('route started')
if __name__ == '__main__': cli()
