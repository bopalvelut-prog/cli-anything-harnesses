import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('assent running')
@cli.command()
def start(): click.echo('assent started')
if __name__ == '__main__': cli()
