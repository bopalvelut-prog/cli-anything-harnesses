import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('prayer running')
@cli.command()
def start(): click.echo('prayer started')
if __name__ == '__main__': cli()
