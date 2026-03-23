import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cash running')
@cli.command()
def start(): click.echo('cash started')
if __name__ == '__main__': cli()
