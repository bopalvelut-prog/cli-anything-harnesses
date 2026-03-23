import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pray running')
@cli.command()
def start(): click.echo('pray started')
if __name__ == '__main__': cli()
