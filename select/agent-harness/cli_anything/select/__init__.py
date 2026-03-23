import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('select running')
@cli.command()
def start(): click.echo('select started')
if __name__ == '__main__': cli()
