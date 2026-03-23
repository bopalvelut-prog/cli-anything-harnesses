import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('libmysql running')
@cli.command()
def start(): click.echo('libmysql started')
if __name__ == '__main__': cli()
