import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mockery running')
@cli.command()
def start(): click.echo('mockery started')
if __name__ == '__main__': cli()
