import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('argoproj running')
@cli.command()
def start(): click.echo('argoproj started')
if __name__ == '__main__': cli()
