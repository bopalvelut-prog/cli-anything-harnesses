import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tender running')
@cli.command()
def start(): click.echo('tender started')
if __name__ == '__main__': cli()
