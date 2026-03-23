import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('oltp running')
@cli.command()
def start(): click.echo('oltp started')
if __name__ == '__main__': cli()
