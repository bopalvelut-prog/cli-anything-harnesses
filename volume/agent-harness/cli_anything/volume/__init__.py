import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('volume running')
@cli.command()
def start(): click.echo('volume started')
if __name__ == '__main__': cli()
