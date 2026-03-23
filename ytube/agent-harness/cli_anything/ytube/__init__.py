import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ytube running')
@cli.command()
def start(): click.echo('ytube started')
if __name__ == '__main__': cli()
