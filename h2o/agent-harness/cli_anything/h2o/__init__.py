import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('h2o running')
@cli.command()
def start(): click.echo('h2o started')
if __name__ == '__main__': cli()
