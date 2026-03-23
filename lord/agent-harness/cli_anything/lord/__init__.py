import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lord running')
@cli.command()
def start(): click.echo('lord started')
if __name__ == '__main__': cli()
