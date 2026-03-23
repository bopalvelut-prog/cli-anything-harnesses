import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kill running')
@cli.command()
def start(): click.echo('kill started')
if __name__ == '__main__': cli()
