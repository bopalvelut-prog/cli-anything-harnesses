import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pass running')
@cli.command()
def start(): click.echo('pass started')
if __name__ == '__main__': cli()
