import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('drop running')
@cli.command()
def start(): click.echo('drop started')
if __name__ == '__main__': cli()
