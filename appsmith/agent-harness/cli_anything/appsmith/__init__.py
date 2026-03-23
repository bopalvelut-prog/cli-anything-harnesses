import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('appsmith running')
@cli.command()
def start(): click.echo('appsmith started')
if __name__ == '__main__': cli()
