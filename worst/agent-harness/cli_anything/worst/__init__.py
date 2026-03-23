import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('worst running')
@cli.command()
def start(): click.echo('worst started')
if __name__ == '__main__': cli()
