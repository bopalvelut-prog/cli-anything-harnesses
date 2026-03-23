import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('financial running')
@cli.command()
def start(): click.echo('financial started')
if __name__ == '__main__': cli()
