import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('armadillo running')
@cli.command()
def start(): click.echo('armadillo started')
if __name__ == '__main__': cli()
