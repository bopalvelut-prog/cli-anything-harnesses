import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('prophet running')
@cli.command()
def start(): click.echo('prophet started')
if __name__ == '__main__': cli()
