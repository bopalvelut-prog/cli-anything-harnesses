import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('popeye running')
@cli.command()
def start(): click.echo('popeye started')
if __name__ == '__main__': cli()
