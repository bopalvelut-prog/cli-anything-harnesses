import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('king running')
@cli.command()
def start(): click.echo('king started')
if __name__ == '__main__': cli()
