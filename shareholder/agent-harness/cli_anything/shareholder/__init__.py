import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shareholder running')
@cli.command()
def start(): click.echo('shareholder started')
if __name__ == '__main__': cli()
