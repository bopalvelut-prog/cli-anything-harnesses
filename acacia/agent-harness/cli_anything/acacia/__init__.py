import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('acacia running')
@cli.command()
def start(): click.echo('acacia started')
if __name__ == '__main__': cli()
