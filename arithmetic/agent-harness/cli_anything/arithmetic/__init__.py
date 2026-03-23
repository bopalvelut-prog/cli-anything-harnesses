import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('arithmetic running')
@cli.command()
def start(): click.echo('arithmetic started')
if __name__ == '__main__': cli()
