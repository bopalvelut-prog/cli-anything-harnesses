import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('learn running')
@cli.command()
def start(): click.echo('learn started')
if __name__ == '__main__': cli()
