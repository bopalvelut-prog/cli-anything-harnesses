import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sustain running')
@cli.command()
def start(): click.echo('sustain started')
if __name__ == '__main__': cli()
