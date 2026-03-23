import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mockito running')
@cli.command()
def start(): click.echo('mockito started')
if __name__ == '__main__': cli()
