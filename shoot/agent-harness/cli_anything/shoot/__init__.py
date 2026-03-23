import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shoot running')
@cli.command()
def start(): click.echo('shoot started')
if __name__ == '__main__': cli()
