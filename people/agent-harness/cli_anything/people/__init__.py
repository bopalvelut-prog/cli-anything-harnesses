import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('people running')
@cli.command()
def start(): click.echo('people started')
if __name__ == '__main__': cli()
