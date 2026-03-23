import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('grand_central running')
@cli.command()
def start(): click.echo('grand_central started')
if __name__ == '__main__': cli()
