import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('date running')
@cli.command()
def start(): click.echo('date started')
if __name__ == '__main__': cli()
