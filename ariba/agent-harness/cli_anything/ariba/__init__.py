import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ariba running')
@cli.command()
def start(): click.echo('ariba started')
if __name__ == '__main__': cli()
