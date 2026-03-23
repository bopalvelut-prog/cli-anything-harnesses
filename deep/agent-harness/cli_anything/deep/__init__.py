import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('deep running')
@cli.command()
def start(): click.echo('deep started')
if __name__ == '__main__': cli()
