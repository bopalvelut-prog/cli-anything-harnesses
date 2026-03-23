import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('young running')
@cli.command()
def start(): click.echo('young started')
if __name__ == '__main__': cli()
