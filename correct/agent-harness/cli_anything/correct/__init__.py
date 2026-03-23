import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('correct running')
@cli.command()
def start(): click.echo('correct started')
if __name__ == '__main__': cli()
