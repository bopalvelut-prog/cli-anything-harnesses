import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('altair running')
@cli.command()
def start(): click.echo('altair started')
if __name__ == '__main__': cli()
