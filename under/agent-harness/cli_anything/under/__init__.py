import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('under running')
@cli.command()
def start(): click.echo('under started')
if __name__ == '__main__': cli()
