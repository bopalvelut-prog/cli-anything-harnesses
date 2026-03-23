import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('justify running')
@cli.command()
def start(): click.echo('justify started')
if __name__ == '__main__': cli()
