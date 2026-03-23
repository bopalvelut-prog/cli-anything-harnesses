import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gaze running')
@cli.command()
def start(): click.echo('gaze started')
if __name__ == '__main__': cli()
