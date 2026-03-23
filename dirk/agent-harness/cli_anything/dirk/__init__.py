import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dirk running')
@cli.command()
def start(): click.echo('dirk started')
if __name__ == '__main__': cli()
