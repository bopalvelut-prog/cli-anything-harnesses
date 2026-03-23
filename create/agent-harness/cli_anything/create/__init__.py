import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('create running')
@cli.command()
def start(): click.echo('create started')
if __name__ == '__main__': cli()
