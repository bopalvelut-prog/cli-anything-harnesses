import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fifty running')
@cli.command()
def start(): click.echo('fifty started')
if __name__ == '__main__': cli()
