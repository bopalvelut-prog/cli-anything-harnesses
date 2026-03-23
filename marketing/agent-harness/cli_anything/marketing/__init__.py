import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('marketing running')
@cli.command()
def start(): click.echo('marketing started')
if __name__ == '__main__': cli()
