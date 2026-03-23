import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sheet running')
@cli.command()
def start(): click.echo('sheet started')
if __name__ == '__main__': cli()
