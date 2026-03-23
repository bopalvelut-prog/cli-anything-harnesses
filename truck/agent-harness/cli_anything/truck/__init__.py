import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('truck running')
@cli.command()
def start(): click.echo('truck started')
if __name__ == '__main__': cli()
