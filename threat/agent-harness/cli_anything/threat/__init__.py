import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('threat running')
@cli.command()
def start(): click.echo('threat started')
if __name__ == '__main__': cli()
