import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('scrap running')
@cli.command()
def start(): click.echo('scrap started')
if __name__ == '__main__': cli()
