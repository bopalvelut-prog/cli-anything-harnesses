import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('column running')
@cli.command()
def start(): click.echo('column started')
if __name__ == '__main__': cli()
