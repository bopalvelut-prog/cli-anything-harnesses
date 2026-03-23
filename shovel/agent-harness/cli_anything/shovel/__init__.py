import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shovel running')
@cli.command()
def start(): click.echo('shovel started')
if __name__ == '__main__': cli()
