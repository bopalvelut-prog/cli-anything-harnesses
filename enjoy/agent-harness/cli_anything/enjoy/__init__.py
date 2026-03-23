import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('enjoy running')
@cli.command()
def start(): click.echo('enjoy started')
if __name__ == '__main__': cli()
