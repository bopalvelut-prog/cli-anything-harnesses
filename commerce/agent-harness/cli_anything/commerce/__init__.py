import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('commerce running')
@cli.command()
def start(): click.echo('commerce started')
if __name__ == '__main__': cli()
