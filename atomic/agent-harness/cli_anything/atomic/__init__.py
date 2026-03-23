import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('atomic running')
@cli.command()
def start(): click.echo('atomic started')
if __name__ == '__main__': cli()
