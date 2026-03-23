import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('broadcom running')
@cli.command()
def start(): click.echo('broadcom started')
if __name__ == '__main__': cli()
