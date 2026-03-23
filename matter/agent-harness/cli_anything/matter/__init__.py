import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('matter running')
@cli.command()
def start(): click.echo('matter started')
if __name__ == '__main__': cli()
