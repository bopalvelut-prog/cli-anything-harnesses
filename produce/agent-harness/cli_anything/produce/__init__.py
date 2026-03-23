import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('produce running')
@cli.command()
def start(): click.echo('produce started')
if __name__ == '__main__': cli()
