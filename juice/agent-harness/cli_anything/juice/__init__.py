import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('juice running')
@cli.command()
def start(): click.echo('juice started')
if __name__ == '__main__': cli()
