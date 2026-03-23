import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('inotifywait running')
@cli.command()
def start(): click.echo('inotifywait started')
if __name__ == '__main__': cli()
