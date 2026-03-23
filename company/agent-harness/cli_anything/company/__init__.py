import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('company running')
@cli.command()
def start(): click.echo('company started')
if __name__ == '__main__': cli()
