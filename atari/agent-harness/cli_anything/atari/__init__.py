import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('atari running')
@cli.command()
def start(): click.echo('atari started')
if __name__ == '__main__': cli()
