import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sister running')
@cli.command()
def start(): click.echo('sister started')
if __name__ == '__main__': cli()
