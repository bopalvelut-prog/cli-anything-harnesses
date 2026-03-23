import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('scikit running')
@cli.command()
def start(): click.echo('scikit started')
if __name__ == '__main__': cli()
