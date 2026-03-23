import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('somewhere running')
@cli.command()
def start(): click.echo('somewhere started')
if __name__ == '__main__': cli()
