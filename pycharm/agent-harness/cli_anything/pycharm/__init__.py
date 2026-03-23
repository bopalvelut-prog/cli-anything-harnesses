import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pycharm running')
@cli.command()
def start(): click.echo('pycharm started')
if __name__ == '__main__': cli()
