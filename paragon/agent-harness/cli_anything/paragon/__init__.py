import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('paragon running')
@cli.command()
def start(): click.echo('paragon started')
if __name__ == '__main__': cli()
