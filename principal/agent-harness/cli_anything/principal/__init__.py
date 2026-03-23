import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('principal running')
@cli.command()
def start(): click.echo('principal started')
if __name__ == '__main__': cli()
