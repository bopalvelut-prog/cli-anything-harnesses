import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('autorest running')
@cli.command()
def start(): click.echo('autorest started')
if __name__ == '__main__': cli()
