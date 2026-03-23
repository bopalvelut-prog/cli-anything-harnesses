import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('driver running')
@cli.command()
def start(): click.echo('driver started')
if __name__ == '__main__': cli()
