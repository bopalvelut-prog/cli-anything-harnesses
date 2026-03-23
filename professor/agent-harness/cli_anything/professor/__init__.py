import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('professor running')
@cli.command()
def start(): click.echo('professor started')
if __name__ == '__main__': cli()
