import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('chase running')
@cli.command()
def start(): click.echo('chase started')
if __name__ == '__main__': cli()
