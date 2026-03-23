import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('authority running')
@cli.command()
def start(): click.echo('authority started')
if __name__ == '__main__': cli()
