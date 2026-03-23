import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('figure running')
@cli.command()
def start(): click.echo('figure started')
if __name__ == '__main__': cli()
