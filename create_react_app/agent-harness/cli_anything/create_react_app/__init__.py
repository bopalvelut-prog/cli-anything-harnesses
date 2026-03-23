import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('create_react_app running')
@cli.command()
def start(): click.echo('create_react_app started')
if __name__ == '__main__': cli()
