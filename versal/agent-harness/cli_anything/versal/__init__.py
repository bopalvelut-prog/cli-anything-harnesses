import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('versal running')
@cli.command()
def start(): click.echo('versal started')
if __name__ == '__main__': cli()
