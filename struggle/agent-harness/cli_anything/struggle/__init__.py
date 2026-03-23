import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('struggle running')
@cli.command()
def start(): click.echo('struggle started')
if __name__ == '__main__': cli()
