import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('earth running')
@cli.command()
def start(): click.echo('earth started')
if __name__ == '__main__': cli()
