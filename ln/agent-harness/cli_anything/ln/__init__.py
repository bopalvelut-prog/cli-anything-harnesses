import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ln running')
@cli.command()
def start(): click.echo('ln started')
if __name__ == '__main__': cli()
