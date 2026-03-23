import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mean running')
@cli.command()
def start(): click.echo('mean started')
if __name__ == '__main__': cli()
