import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('assist running')
@cli.command()
def start(): click.echo('assist started')
if __name__ == '__main__': cli()
