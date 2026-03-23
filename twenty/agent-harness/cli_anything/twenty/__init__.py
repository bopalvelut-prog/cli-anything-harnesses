import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('twenty running')
@cli.command()
def start(): click.echo('twenty started')
if __name__ == '__main__': cli()
