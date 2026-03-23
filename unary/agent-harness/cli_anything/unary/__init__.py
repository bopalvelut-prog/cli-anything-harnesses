import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('unary running')
@cli.command()
def start(): click.echo('unary started')
if __name__ == '__main__': cli()
