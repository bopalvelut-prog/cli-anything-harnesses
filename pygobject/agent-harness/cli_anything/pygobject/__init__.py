import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pygobject running')
@cli.command()
def start(): click.echo('pygobject started')
if __name__ == '__main__': cli()
