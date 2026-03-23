import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('deepstream running')
@cli.command()
def start(): click.echo('deepstream started')
if __name__ == '__main__': cli()
