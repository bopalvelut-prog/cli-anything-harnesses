import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('astroid running')
@cli.command()
def start(): click.echo('astroid started')
if __name__ == '__main__': cli()
