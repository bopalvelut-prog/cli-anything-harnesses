import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('core running')
@cli.command()
def start(): click.echo('core started')
if __name__ == '__main__': cli()
