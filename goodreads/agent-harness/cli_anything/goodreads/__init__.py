import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('goodreads running')
@cli.command()
def start(): click.echo('goodreads started')
if __name__ == '__main__': cli()
