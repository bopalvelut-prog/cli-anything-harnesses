import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('order running')
@cli.command()
def start(): click.echo('order started')
if __name__ == '__main__': cli()
