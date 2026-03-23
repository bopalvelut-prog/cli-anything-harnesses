import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('include running')
@cli.command()
def start(): click.echo('include started')
if __name__ == '__main__': cli()
