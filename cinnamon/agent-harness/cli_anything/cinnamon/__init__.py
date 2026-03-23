import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cinnamon running')
@cli.command()
def start(): click.echo('cinnamon started')
if __name__ == '__main__': cli()
