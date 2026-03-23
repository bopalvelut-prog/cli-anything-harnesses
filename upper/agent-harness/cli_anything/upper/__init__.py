import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('upper running')
@cli.command()
def start(): click.echo('upper started')
if __name__ == '__main__': cli()
