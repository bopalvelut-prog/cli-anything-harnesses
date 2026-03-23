import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bless running')
@cli.command()
def start(): click.echo('bless started')
if __name__ == '__main__': cli()
