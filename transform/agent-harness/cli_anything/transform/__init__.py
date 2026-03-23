import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('transform running')
@cli.command()
def start(): click.echo('transform started')
if __name__ == '__main__': cli()
