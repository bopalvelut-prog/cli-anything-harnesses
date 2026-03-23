import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('concern running')
@cli.command()
def start(): click.echo('concern started')
if __name__ == '__main__': cli()
