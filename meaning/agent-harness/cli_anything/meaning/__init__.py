import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('meaning running')
@cli.command()
def start(): click.echo('meaning started')
if __name__ == '__main__': cli()
