import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ops running')
@cli.command()
def start(): click.echo('ops started')
if __name__ == '__main__': cli()
