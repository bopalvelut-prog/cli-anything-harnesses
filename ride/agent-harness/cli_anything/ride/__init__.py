import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ride running')
@cli.command()
def start(): click.echo('ride started')
if __name__ == '__main__': cli()
