import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('vendor running')
@cli.command()
def start(): click.echo('vendor started')
if __name__ == '__main__': cli()
