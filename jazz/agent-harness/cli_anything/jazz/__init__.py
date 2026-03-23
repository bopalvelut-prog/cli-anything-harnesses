import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jazz running')
@cli.command()
def start(): click.echo('jazz started')
if __name__ == '__main__': cli()
