import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sensu running')
@cli.command()
def start(): click.echo('sensu started')
if __name__ == '__main__': cli()
