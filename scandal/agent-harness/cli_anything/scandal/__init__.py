import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('scandal running')
@cli.command()
def start(): click.echo('scandal started')
if __name__ == '__main__': cli()
