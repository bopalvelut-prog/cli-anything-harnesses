import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('priority running')
@cli.command()
def start(): click.echo('priority started')
if __name__ == '__main__': cli()
