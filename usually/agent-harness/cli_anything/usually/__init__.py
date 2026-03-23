import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('usually running')
@cli.command()
def start(): click.echo('usually started')
if __name__ == '__main__': cli()
