import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('five running')
@cli.command()
def start(): click.echo('five started')
if __name__ == '__main__': cli()
