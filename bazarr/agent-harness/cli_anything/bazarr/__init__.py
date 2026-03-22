import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Bazarr status')
@cli.command()
def subtitles(): click.echo('Subtitles')
if __name__ == '__main__': cli()
