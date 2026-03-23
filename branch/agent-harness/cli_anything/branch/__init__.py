import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('branch running')
@cli.command()
def start(): click.echo('branch started')
if __name__ == '__main__': cli()
