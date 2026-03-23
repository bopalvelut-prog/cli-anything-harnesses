import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('yahoo running')
@cli.command()
def start(): click.echo('yahoo started')
if __name__ == '__main__': cli()
