import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('medicine running')
@cli.command()
def start(): click.echo('medicine started')
if __name__ == '__main__': cli()
