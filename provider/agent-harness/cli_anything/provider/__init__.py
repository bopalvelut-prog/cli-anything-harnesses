import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('provider running')
@cli.command()
def start(): click.echo('provider started')
if __name__ == '__main__': cli()
