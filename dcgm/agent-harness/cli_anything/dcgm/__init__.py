import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dcgm running')
@cli.command()
def start(): click.echo('dcgm started')
if __name__ == '__main__': cli()
