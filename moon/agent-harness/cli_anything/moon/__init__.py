import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('moon running')
@cli.command()
def start(): click.echo('moon started')
if __name__ == '__main__': cli()
