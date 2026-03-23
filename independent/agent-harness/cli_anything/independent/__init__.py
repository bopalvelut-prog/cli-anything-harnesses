import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('independent running')
@cli.command()
def start(): click.echo('independent started')
if __name__ == '__main__': cli()
