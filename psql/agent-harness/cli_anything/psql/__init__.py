import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('psql running')
@cli.command()
def start(): click.echo('psql started')
if __name__ == '__main__': cli()
