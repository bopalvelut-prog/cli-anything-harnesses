import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('unity running')
@cli.command()
def start(): click.echo('unity started')
if __name__ == '__main__': cli()
