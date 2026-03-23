import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('flight running')
@cli.command()
def start(): click.echo('flight started')
if __name__ == '__main__': cli()
