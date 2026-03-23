import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('choice running')
@cli.command()
def start(): click.echo('choice started')
if __name__ == '__main__': cli()
