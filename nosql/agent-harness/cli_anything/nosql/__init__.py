import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nosql running')
@cli.command()
def start(): click.echo('nosql started')
if __name__ == '__main__': cli()
