import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tour running')
@cli.command()
def start(): click.echo('tour started')
if __name__ == '__main__': cli()
