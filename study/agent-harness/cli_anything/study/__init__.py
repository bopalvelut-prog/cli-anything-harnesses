import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('study running')
@cli.command()
def start(): click.echo('study started')
if __name__ == '__main__': cli()
