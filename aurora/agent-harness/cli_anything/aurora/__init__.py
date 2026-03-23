import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aurora running')
@cli.command()
def start(): click.echo('aurora started')
if __name__ == '__main__': cli()
