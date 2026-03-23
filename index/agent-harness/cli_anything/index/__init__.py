import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('index running')
@cli.command()
def start(): click.echo('index started')
if __name__ == '__main__': cli()
