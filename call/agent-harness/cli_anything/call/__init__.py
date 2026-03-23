import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('call running')
@cli.command()
def start(): click.echo('call started')
if __name__ == '__main__': cli()
