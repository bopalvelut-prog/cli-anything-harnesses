import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('charon running')
@cli.command()
def start(): click.echo('charon started')
if __name__ == '__main__': cli()
