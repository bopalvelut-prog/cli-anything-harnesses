import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('zombie running')
@cli.command()
def start(): click.echo('zombie started')
if __name__ == '__main__': cli()
