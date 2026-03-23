import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('virus running')
@cli.command()
def start(): click.echo('virus started')
if __name__ == '__main__': cli()
