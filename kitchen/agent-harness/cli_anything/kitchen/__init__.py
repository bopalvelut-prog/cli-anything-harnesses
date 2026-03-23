import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kitchen running')
@cli.command()
def start(): click.echo('kitchen started')
if __name__ == '__main__': cli()
