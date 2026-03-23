import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('network running')
@cli.command()
def start(): click.echo('network started')
if __name__ == '__main__': cli()
