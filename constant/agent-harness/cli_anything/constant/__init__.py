import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('constant running')
@cli.command()
def start(): click.echo('constant started')
if __name__ == '__main__': cli()
