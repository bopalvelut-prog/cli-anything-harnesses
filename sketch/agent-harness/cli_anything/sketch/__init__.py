import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sketch running')
@cli.command()
def start(): click.echo('sketch started')
if __name__ == '__main__': cli()
