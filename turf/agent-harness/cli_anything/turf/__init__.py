import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('turf running')
@cli.command()
def start(): click.echo('turf started')
if __name__ == '__main__': cli()
