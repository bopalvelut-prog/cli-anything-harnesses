import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dollar running')
@cli.command()
def start(): click.echo('dollar started')
if __name__ == '__main__': cli()
