import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('automl running')
@cli.command()
def start(): click.echo('automl started')
if __name__ == '__main__': cli()
