import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('alpakka running')
@cli.command()
def start(): click.echo('alpakka started')
if __name__ == '__main__': cli()
