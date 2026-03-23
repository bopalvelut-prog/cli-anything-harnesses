import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('terminus running')
@cli.command()
def start(): click.echo('terminus started')
if __name__ == '__main__': cli()
