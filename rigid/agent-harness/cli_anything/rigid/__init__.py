import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rigid running')
@cli.command()
def start(): click.echo('rigid started')
if __name__ == '__main__': cli()
