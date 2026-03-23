import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('source running')
@cli.command()
def start(): click.echo('source started')
if __name__ == '__main__': cli()
