import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('perhaps running')
@cli.command()
def start(): click.echo('perhaps started')
if __name__ == '__main__': cli()
