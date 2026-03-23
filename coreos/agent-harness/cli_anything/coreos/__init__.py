import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('coreos running')
@cli.command()
def start(): click.echo('coreos started')
if __name__ == '__main__': cli()
