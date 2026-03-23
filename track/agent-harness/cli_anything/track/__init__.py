import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('track running')
@cli.command()
def start(): click.echo('track started')
if __name__ == '__main__': cli()
