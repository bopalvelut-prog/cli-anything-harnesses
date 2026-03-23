import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('blade running')
@cli.command()
def start(): click.echo('blade started')
if __name__ == '__main__': cli()
