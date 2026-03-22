
import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('media')
def play(media): subprocess.run(['cvlc', media, '--play-and-exit']); click.echo('Playing')
@cli.command()
@click.argument('url')
def stream(url): subprocess.run(['cvlc', url, '--sout', '#std{access=http,mux=ts,dst=:8080}'])
if __name__ == '__main__': cli()
