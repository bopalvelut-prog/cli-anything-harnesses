import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('metronome running')
@cli.command()
def start(): click.echo('metronome started')
if __name__ == '__main__': cli()
