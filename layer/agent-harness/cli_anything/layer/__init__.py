import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('layer running')
@cli.command()
def start(): click.echo('layer started')
if __name__ == '__main__': cli()
