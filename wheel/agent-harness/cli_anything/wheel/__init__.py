import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wheel running')
@cli.command()
def start(): click.echo('wheel started')
if __name__ == '__main__': cli()
