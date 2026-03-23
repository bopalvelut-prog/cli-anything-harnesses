import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rtsp running')
@cli.command()
def start(): click.echo('rtsp started')
if __name__ == '__main__': cli()
