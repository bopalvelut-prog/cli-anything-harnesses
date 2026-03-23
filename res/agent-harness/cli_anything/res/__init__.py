import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('res running')
@cli.command()
def start(): click.echo('res started')
if __name__ == '__main__': cli()
