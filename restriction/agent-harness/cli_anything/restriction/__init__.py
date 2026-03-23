import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('restriction running')
@cli.command()
def start(): click.echo('restriction started')
if __name__ == '__main__': cli()
