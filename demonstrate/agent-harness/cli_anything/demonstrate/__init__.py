import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('demonstrate running')
@cli.command()
def start(): click.echo('demonstrate started')
if __name__ == '__main__': cli()
