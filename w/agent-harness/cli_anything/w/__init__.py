import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('w running')
@cli.command()
def start(): click.echo('w started')
if __name__ == '__main__': cli()
