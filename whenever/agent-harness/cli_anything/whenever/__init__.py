import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('whenever running')
@cli.command()
def start(): click.echo('whenever started')
if __name__ == '__main__': cli()
