import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('personal running')
@cli.command()
def start(): click.echo('personal started')
if __name__ == '__main__': cli()
