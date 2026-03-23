import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mp3 running')
@cli.command()
def start(): click.echo('mp3 started')
if __name__ == '__main__': cli()
