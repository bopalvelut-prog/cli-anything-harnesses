import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('flush running')
@cli.command()
def start(): click.echo('flush started')
if __name__ == '__main__': cli()
