import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rx running')
@cli.command()
def start(): click.echo('rx started')
if __name__ == '__main__': cli()
