import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tan running')
@cli.command()
def start(): click.echo('tan started')
if __name__ == '__main__': cli()
