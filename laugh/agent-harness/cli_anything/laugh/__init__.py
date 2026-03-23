import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('laugh running')
@cli.command()
def start(): click.echo('laugh started')
if __name__ == '__main__': cli()
