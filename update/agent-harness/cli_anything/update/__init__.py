import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('update running')
@cli.command()
def start(): click.echo('update started')
if __name__ == '__main__': cli()
