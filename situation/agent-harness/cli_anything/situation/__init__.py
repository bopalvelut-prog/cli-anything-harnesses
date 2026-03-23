import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('situation running')
@cli.command()
def start(): click.echo('situation started')
if __name__ == '__main__': cli()
