import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aspen running')
@cli.command()
def start(): click.echo('aspen started')
if __name__ == '__main__': cli()
