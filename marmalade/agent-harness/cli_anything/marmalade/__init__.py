import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('marmalade running')
@cli.command()
def start(): click.echo('marmalade started')
if __name__ == '__main__': cli()
