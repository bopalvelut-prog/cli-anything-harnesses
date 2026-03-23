import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sing running')
@cli.command()
def start(): click.echo('sing started')
if __name__ == '__main__': cli()
