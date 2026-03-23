import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('edition running')
@cli.command()
def start(): click.echo('edition started')
if __name__ == '__main__': cli()
