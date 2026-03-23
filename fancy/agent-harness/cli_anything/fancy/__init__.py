import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fancy running')
@cli.command()
def start(): click.echo('fancy started')
if __name__ == '__main__': cli()
