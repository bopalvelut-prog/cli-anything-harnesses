import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cloudify running')
@cli.command()
def start(): click.echo('cloudify started')
if __name__ == '__main__': cli()
