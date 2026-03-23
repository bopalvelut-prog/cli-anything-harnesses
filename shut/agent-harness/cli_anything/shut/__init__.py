import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shut running')
@cli.command()
def start(): click.echo('shut started')
if __name__ == '__main__': cli()
