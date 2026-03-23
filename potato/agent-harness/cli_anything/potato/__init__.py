import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('potato running')
@cli.command()
def start(): click.echo('potato started')
if __name__ == '__main__': cli()
