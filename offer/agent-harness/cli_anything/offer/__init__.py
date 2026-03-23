import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('offer running')
@cli.command()
def start(): click.echo('offer started')
if __name__ == '__main__': cli()
