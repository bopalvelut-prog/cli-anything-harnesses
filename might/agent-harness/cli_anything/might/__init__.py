import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('might running')
@cli.command()
def start(): click.echo('might started')
if __name__ == '__main__': cli()
