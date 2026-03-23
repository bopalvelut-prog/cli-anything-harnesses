import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ground running')
@cli.command()
def start(): click.echo('ground started')
if __name__ == '__main__': cli()
