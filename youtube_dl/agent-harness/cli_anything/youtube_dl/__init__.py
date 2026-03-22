import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('url')
def download(url): subprocess.run(['yt-dlp', url])
@cli.command()
@click.argument('url')
def audio(url): subprocess.run(['yt-dlp', '-x', '--audio-format', 'mp3', url])
@cli.command()
@click.argument('url')
def playlist(url): subprocess.run(['yt-dlp', '--yes-playlist', url])
if __name__ == '__main__': cli()
