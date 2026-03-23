import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('changelogs running')
@cli.command()
def start(): click.echo('changelogs started')
if __name__ == '__main__': cli()
