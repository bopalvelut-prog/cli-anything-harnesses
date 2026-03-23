import click
@click.group()
def cli(): pass
@cli.command()
def tts(): click.echo('ElevenLabs TTS')
@cli.command()
def voices(): click.echo('ElevenLabs voices')
if __name__ == '__main__': cli()
