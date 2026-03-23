import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('qualify running')
@cli.command()
def start(): click.echo('qualify started')
if __name__ == '__main__': cli()
