import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('trait running')
@cli.command()
def start(): click.echo('trait started')
if __name__ == '__main__': cli()
