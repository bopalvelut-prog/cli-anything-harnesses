import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('home running')
@cli.command()
def start(): click.echo('home started')
if __name__ == '__main__': cli()
