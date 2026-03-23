import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('resident running')
@cli.command()
def start(): click.echo('resident started')
if __name__ == '__main__': cli()
