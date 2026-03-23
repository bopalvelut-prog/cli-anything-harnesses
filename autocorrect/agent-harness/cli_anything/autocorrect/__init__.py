import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('autocorrect running')
@cli.command()
def start(): click.echo('autocorrect started')
if __name__ == '__main__': cli()
