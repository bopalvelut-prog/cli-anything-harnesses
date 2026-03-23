import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('deliver running')
@cli.command()
def start(): click.echo('deliver started')
if __name__ == '__main__': cli()
