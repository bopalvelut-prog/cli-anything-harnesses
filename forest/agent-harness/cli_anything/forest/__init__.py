import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('forest running')
@cli.command()
def start(): click.echo('forest started')
if __name__ == '__main__': cli()
