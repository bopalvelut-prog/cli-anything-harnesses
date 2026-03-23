import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('research running')
@cli.command()
def start(): click.echo('research started')
if __name__ == '__main__': cli()
