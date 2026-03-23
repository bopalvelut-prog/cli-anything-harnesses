import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tail running')
@cli.command()
def start(): click.echo('tail started')
if __name__ == '__main__': cli()
