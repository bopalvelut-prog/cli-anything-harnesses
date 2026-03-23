import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('octave running')
@cli.command()
def start(): click.echo('octave started')
if __name__ == '__main__': cli()
