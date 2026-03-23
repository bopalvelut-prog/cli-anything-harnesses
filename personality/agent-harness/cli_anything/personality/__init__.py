import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('personality running')
@cli.command()
def start(): click.echo('personality started')
if __name__ == '__main__': cli()
