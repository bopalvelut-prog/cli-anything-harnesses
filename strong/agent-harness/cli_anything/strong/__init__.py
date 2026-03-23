import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('strong running')
@cli.command()
def start(): click.echo('strong started')
if __name__ == '__main__': cli()
