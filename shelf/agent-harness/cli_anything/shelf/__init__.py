import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shelf running')
@cli.command()
def start(): click.echo('shelf started')
if __name__ == '__main__': cli()
