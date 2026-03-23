import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('input running')
@cli.command()
def start(): click.echo('input started')
if __name__ == '__main__': cli()
