import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('clay running')
@cli.command()
def start(): click.echo('clay started')
if __name__ == '__main__': cli()
