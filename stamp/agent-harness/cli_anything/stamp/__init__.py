import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stamp running')
@cli.command()
def start(): click.echo('stamp started')
if __name__ == '__main__': cli()
