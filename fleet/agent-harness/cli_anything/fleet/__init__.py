import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fleet running')
@cli.command()
def start(): click.echo('fleet started')
if __name__ == '__main__': cli()
