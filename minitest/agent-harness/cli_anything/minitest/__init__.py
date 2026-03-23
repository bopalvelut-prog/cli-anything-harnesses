import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('minitest running')
@cli.command()
def start(): click.echo('minitest started')
if __name__ == '__main__': cli()
