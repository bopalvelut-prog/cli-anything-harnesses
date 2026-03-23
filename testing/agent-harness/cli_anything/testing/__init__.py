import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('testing running')
@cli.command()
def start(): click.echo('testing started')
if __name__ == '__main__': cli()
