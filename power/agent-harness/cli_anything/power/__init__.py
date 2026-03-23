import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('power running')
@cli.command()
def start(): click.echo('power started')
if __name__ == '__main__': cli()
