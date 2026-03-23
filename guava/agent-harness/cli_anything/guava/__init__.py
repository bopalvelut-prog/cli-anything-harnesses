import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('guava running')
@cli.command()
def start(): click.echo('guava started')
if __name__ == '__main__': cli()
