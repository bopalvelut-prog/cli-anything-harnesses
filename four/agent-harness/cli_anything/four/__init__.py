import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('four running')
@cli.command()
def start(): click.echo('four started')
if __name__ == '__main__': cli()
