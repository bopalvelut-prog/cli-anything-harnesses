import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dlmalloc running')
@cli.command()
def start(): click.echo('dlmalloc started')
if __name__ == '__main__': cli()
