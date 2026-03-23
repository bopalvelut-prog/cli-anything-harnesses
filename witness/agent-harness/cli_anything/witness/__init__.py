import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('witness running')
@cli.command()
def start(): click.echo('witness started')
if __name__ == '__main__': cli()
