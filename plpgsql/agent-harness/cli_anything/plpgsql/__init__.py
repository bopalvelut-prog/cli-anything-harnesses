import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('plpgsql running')
@cli.command()
def start(): click.echo('plpgsql started')
if __name__ == '__main__': cli()
