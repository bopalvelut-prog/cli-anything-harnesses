import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('autocode running')
@cli.command()
def start(): click.echo('autocode started')
if __name__ == '__main__': cli()
