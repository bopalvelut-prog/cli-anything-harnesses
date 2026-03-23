import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('appcenter running')
@cli.command()
def start(): click.echo('appcenter started')
if __name__ == '__main__': cli()
