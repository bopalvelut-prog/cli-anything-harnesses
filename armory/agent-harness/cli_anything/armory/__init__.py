import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('armory running')
@cli.command()
def start(): click.echo('armory started')
if __name__ == '__main__': cli()
