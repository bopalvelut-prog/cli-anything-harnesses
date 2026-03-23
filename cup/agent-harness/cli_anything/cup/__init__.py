import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cup running')
@cli.command()
def start(): click.echo('cup started')
if __name__ == '__main__': cli()
