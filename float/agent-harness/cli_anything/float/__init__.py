import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('float running')
@cli.command()
def start(): click.echo('float started')
if __name__ == '__main__': cli()
