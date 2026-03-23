import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('musical running')
@cli.command()
def start(): click.echo('musical started')
if __name__ == '__main__': cli()
