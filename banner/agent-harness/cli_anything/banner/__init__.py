import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('banner running')
@cli.command()
def start(): click.echo('banner started')
if __name__ == '__main__': cli()
