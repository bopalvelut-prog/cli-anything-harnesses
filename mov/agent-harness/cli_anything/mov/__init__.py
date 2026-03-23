import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mov running')
@cli.command()
def start(): click.echo('mov started')
if __name__ == '__main__': cli()
