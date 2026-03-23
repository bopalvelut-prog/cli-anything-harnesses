import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stack running')
@cli.command()
def start(): click.echo('stack started')
if __name__ == '__main__': cli()
