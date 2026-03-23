import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('somebody running')
@cli.command()
def start(): click.echo('somebody started')
if __name__ == '__main__': cli()
