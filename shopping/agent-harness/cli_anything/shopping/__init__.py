import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shopping running')
@cli.command()
def start(): click.echo('shopping started')
if __name__ == '__main__': cli()
