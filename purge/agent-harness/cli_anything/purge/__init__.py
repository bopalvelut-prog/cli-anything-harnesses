import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('purge running')
@cli.command()
def start(): click.echo('purge started')
if __name__ == '__main__': cli()
