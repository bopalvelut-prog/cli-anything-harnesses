import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cattle running')
@cli.command()
def start(): click.echo('cattle started')
if __name__ == '__main__': cli()
