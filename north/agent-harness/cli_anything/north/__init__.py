import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('north running')
@cli.command()
def start(): click.echo('north started')
if __name__ == '__main__': cli()
