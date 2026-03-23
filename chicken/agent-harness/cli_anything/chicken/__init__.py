import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('chicken running')
@cli.command()
def start(): click.echo('chicken started')
if __name__ == '__main__': cli()
