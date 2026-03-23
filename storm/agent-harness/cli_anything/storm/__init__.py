import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('storm running')
@cli.command()
def start(): click.echo('storm started')
if __name__ == '__main__': cli()
