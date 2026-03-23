import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bird running')
@cli.command()
def start(): click.echo('bird started')
if __name__ == '__main__': cli()
