import click
@click.group()
def cli(): pass
@cli.command()
def transcribe(): click.echo('Whisper transcribe')
@cli.command()
def translate(): click.echo('Whisper translate')
if __name__ == '__main__': cli()
