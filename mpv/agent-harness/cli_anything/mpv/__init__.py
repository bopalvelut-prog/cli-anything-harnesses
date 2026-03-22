
import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('media')
@click.option('--fullscreen', is_flag=True)
def play(media, fullscreen):
    cmd = ['mpv', media]; subprocess.Popen(cmd); click.echo('Playing')
@cli.command()
@click.argument('url')
def stream(url): subprocess.run(['mpv', url])
if __name__ == '__main__': cli()
