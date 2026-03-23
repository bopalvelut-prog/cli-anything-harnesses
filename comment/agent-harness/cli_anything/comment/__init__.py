import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('comment running')
@cli.command()
def start(): click.echo('comment started')
if __name__ == '__main__': cli()
