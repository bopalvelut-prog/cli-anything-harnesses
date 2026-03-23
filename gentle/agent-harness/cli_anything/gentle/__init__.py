import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gentle running')
@cli.command()
def start(): click.echo('gentle started')
if __name__ == '__main__': cli()
