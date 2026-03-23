import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('perform running')
@cli.command()
def start(): click.echo('perform started')
if __name__ == '__main__': cli()
