import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('spawn running')
@cli.command()
def start(): click.echo('spawn started')
if __name__ == '__main__': cli()
