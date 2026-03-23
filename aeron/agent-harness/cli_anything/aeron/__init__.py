import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aeron running')
@cli.command()
def start(): click.echo('aeron started')
if __name__ == '__main__': cli()
