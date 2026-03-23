import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('glove running')
@cli.command()
def start(): click.echo('glove started')
if __name__ == '__main__': cli()
