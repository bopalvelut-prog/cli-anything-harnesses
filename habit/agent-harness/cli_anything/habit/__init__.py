import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('habit running')
@cli.command()
def start(): click.echo('habit started')
if __name__ == '__main__': cli()
