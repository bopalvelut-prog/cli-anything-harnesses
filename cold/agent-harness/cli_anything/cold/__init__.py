import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cold running')
@cli.command()
def start(): click.echo('cold started')
if __name__ == '__main__': cli()
