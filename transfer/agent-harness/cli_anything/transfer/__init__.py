import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('transfer running')
@cli.command()
def start(): click.echo('transfer started')
if __name__ == '__main__': cli()
