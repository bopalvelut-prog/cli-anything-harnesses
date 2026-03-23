import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('voluntary running')
@cli.command()
def start(): click.echo('voluntary started')
if __name__ == '__main__': cli()
