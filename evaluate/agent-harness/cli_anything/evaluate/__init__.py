import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('evaluate running')
@cli.command()
def start(): click.echo('evaluate started')
if __name__ == '__main__': cli()
