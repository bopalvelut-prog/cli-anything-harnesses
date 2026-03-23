import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('inotify running')
@cli.command()
def start(): click.echo('inotify started')
if __name__ == '__main__': cli()
