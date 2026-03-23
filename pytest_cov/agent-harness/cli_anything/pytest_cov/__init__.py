import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pytest_cov running')
@cli.command()
def start(): click.echo('pytest_cov started')
if __name__ == '__main__': cli()
