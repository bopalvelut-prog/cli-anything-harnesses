import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dry running')
@cli.command()
def start(): click.echo('dry started')
if __name__ == '__main__': cli()
