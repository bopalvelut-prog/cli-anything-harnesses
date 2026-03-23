import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('grief running')
@cli.command()
def start(): click.echo('grief started')
if __name__ == '__main__': cli()
