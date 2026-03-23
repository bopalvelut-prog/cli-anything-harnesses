import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('x running')
@cli.command()
def start(): click.echo('x started')
if __name__ == '__main__': cli()
