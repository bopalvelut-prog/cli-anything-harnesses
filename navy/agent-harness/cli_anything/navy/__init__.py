import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('navy running')
@cli.command()
def start(): click.echo('navy started')
if __name__ == '__main__': cli()
