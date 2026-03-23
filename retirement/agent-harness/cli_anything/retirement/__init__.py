import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('retirement running')
@cli.command()
def start(): click.echo('retirement started')
if __name__ == '__main__': cli()
