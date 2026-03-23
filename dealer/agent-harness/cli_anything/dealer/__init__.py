import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dealer running')
@cli.command()
def start(): click.echo('dealer started')
if __name__ == '__main__': cli()
