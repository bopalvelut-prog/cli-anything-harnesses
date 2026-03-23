import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('satisfy running')
@cli.command()
def start(): click.echo('satisfy started')
if __name__ == '__main__': cli()
