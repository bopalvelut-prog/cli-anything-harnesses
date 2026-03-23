import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('eye running')
@cli.command()
def start(): click.echo('eye started')
if __name__ == '__main__': cli()
