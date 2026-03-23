import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('inner running')
@cli.command()
def start(): click.echo('inner started')
if __name__ == '__main__': cli()
