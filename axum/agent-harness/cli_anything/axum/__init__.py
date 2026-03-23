import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('axum running')
@cli.command()
def start(): click.echo('axum started')
if __name__ == '__main__': cli()
