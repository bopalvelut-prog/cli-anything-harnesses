import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pack running')
@cli.command()
def start(): click.echo('pack started')
if __name__ == '__main__': cli()
