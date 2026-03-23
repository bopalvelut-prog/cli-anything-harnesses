import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ascend running')
@cli.command()
def start(): click.echo('ascend started')
if __name__ == '__main__': cli()
