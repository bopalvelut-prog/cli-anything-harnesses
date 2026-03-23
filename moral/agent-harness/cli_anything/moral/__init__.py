import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('moral running')
@cli.command()
def start(): click.echo('moral started')
if __name__ == '__main__': cli()
