import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('validate running')
@cli.command()
def start(): click.echo('validate started')
if __name__ == '__main__': cli()
