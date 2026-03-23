import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('menu running')
@cli.command()
def start(): click.echo('menu started')
if __name__ == '__main__': cli()
