import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('national running')
@cli.command()
def start(): click.echo('national started')
if __name__ == '__main__': cli()
