import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('planet running')
@cli.command()
def start(): click.echo('planet started')
if __name__ == '__main__': cli()
