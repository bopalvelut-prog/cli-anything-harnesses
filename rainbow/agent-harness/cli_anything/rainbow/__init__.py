import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rainbow running')
@cli.command()
def start(): click.echo('rainbow started')
if __name__ == '__main__': cli()
