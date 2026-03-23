import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('thus running')
@cli.command()
def start(): click.echo('thus started')
if __name__ == '__main__': cli()
