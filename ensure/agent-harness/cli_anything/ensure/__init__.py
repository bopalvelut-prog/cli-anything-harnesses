import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ensure running')
@cli.command()
def start(): click.echo('ensure started')
if __name__ == '__main__': cli()
