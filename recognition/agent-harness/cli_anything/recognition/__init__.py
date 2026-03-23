import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('recognition running')
@cli.command()
def start(): click.echo('recognition started')
if __name__ == '__main__': cli()
