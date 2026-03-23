import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('partly running')
@cli.command()
def start(): click.echo('partly started')
if __name__ == '__main__': cli()
