import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('communicate running')
@cli.command()
def start(): click.echo('communicate started')
if __name__ == '__main__': cli()
