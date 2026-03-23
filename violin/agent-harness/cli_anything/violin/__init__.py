import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('violin running')
@cli.command()
def start(): click.echo('violin started')
if __name__ == '__main__': cli()
