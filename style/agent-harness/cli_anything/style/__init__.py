import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('style running')
@cli.command()
def start(): click.echo('style started')
if __name__ == '__main__': cli()
