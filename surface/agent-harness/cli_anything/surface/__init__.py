import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('surface running')
@cli.command()
def start(): click.echo('surface started')
if __name__ == '__main__': cli()
