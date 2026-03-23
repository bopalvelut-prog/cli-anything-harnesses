import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('portion running')
@cli.command()
def start(): click.echo('portion started')
if __name__ == '__main__': cli()
