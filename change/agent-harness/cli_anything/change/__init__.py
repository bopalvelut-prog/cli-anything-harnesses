import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('change running')
@cli.command()
def start(): click.echo('change started')
if __name__ == '__main__': cli()
