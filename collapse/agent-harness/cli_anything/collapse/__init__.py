import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('collapse running')
@cli.command()
def start(): click.echo('collapse started')
if __name__ == '__main__': cli()
