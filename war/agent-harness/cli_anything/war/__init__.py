import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('war running')
@cli.command()
def start(): click.echo('war started')
if __name__ == '__main__': cli()
