import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('better_sqlite running')
@cli.command()
def start(): click.echo('better_sqlite started')
if __name__ == '__main__': cli()
