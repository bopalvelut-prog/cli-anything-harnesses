import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('keydb running')
@cli.command()
def start(): click.echo('keydb started')
if __name__ == '__main__': cli()
