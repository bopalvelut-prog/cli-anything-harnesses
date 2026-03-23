import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('whisper running')
@cli.command()
def start(): click.echo('whisper started')
if __name__ == '__main__': cli()
