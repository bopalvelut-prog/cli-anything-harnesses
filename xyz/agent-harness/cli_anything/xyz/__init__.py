import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('xyz running')
@cli.command()
def start(): click.echo('xyz started')
if __name__ == '__main__': cli()
