import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('parent running')
@cli.command()
def start(): click.echo('parent started')
if __name__ == '__main__': cli()
