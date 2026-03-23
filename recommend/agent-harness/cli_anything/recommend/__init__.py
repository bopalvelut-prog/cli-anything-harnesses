import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('recommend running')
@cli.command()
def start(): click.echo('recommend started')
if __name__ == '__main__': cli()
