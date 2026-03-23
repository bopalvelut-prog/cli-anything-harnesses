import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sales running')
@cli.command()
def start(): click.echo('sales started')
if __name__ == '__main__': cli()
