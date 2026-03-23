import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pageres running')
@cli.command()
def start(): click.echo('pageres started')
if __name__ == '__main__': cli()
