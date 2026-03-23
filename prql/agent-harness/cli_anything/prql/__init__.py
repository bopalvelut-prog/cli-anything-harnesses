import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('prql running')
@cli.command()
def start(): click.echo('prql started')
if __name__ == '__main__': cli()
