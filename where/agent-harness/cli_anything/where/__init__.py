import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('where running')
@cli.command()
def start(): click.echo('where started')
if __name__ == '__main__': cli()
