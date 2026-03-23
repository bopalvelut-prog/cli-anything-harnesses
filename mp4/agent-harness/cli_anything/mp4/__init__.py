import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mp4 running')
@cli.command()
def start(): click.echo('mp4 started')
if __name__ == '__main__': cli()
