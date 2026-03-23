import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('context running')
@cli.command()
def start(): click.echo('context started')
if __name__ == '__main__': cli()
