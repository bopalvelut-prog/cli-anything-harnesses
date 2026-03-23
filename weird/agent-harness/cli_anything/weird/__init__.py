import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('weird running')
@cli.command()
def start(): click.echo('weird started')
if __name__ == '__main__': cli()
