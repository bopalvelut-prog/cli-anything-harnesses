import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gray running')
@cli.command()
def start(): click.echo('gray started')
if __name__ == '__main__': cli()
