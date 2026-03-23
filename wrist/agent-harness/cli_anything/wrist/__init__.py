import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wrist running')
@cli.command()
def start(): click.echo('wrist started')
if __name__ == '__main__': cli()
