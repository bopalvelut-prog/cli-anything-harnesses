import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('claim running')
@cli.command()
def start(): click.echo('claim started')
if __name__ == '__main__': cli()
