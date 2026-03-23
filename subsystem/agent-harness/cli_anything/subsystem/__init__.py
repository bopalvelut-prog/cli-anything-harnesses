import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('subsystem running')
@cli.command()
def start(): click.echo('subsystem started')
if __name__ == '__main__': cli()
