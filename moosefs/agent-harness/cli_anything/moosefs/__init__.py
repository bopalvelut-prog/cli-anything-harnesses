import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('moosefs running')
@cli.command()
def start(): click.echo('moosefs started')
if __name__ == '__main__': cli()
