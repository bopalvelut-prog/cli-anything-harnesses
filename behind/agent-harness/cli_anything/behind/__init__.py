import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('behind running')
@cli.command()
def start(): click.echo('behind started')
if __name__ == '__main__': cli()
